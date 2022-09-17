from http.client import HTTPResponse
import re
import csv
import json
from rest_framework.views import APIView
from rest_framework import status
from insurance.serializers import *
from http import HTTPStatus
from django.shortcuts import get_list_or_404
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from insurance.models import Members, Organisation

class Organisations(APIView):
    def post(self, request):
        data = request.data.get('items', request.data)
        many = isinstance(data, list)
        serializer = OrganisationSerializer(data=data, many=many)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
        )

    def get(self, request):
        offset, limit = int(request.GET.get("page")), int(request.GET.get("size"))
        queryset = Organisation.objects.prefetch_related('members').all()[offset:offset+limit]
        serializer_class = OrgMemeberSerializer(queryset, many=True)
        return Response(serializer_class.data)

class MembersList(APIView):
    def get(self, request, org_id):
        querset = Members.objects.filter(org_id=int(org_id)).values()
        serializer_class = MembersAllSerializer(querset, many=True)
        return Response(serializer_class.data)

    def post(self, request, org_id):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        names_regex = re.compile(r'(.*[a-z]){3}')
        data = request.data.get('items', request.data)
        ids = Members.objects.values_list("employee_id", flat=True)
        create_objs, rejected_objs = [], []
        counter = 1
        for obj in data:
            reason = {"row_no": counter, "reason": []}
            if obj['employee_id'] not in ids:
                if obj['gender'] in ["Male", "Female", "Others"]:
                    if datetime.strptime(obj['dob'], "%d/%m/%Y"):
                        obj['dob'] = datetime.strptime(obj['dob'], "%d/%m/%Y")
                        obj['dob'] = obj['dob'].strftime('%Y-%m-%d')
                        if len(obj['email'].strip()):
                            if not re.fullmatch(regex, obj['email']):
                                reason['reason'].append("email is invalid")
                            if bool(re.fullmatch(names_regex, obj['first_name'].strip())):
                                if bool(re.fullmatch(names_regex, obj['last_name'].strip())):
                                    create_objs.append(Members(org_id=org_id, employee_id=obj['employee_id'], first_name=obj['first_name'], middle_name=obj['middle_name'], last_name=obj['last_name'], email_id=obj['email'], date_of_birth=obj['dob'], gender=obj['gender']))
                                else:
                                    reason['reason'].append("last name is invalid")
                            else:
                                reason['reason'].append("first name is invalid")
                    else:
                        reason['reason'].appennd("date of birth is invalid")
                else:
                    reason['reason'].append("invalid gender value")
            else:
                if obj['employee_id']:
                    reason['reason'].append("employee_id already exists")
                else:
                    reason['reason'].append("employee_id is empty")
            counter += 1
            rejected_objs.append(reason)
        Members.objects.bulk_create(create_objs)
        return Response(rejected_objs)
