from rest_framework import serializers

from insurance.models import Organisation, Members

class OrganisationSerializer(serializers.ModelSerializer):
   class Meta:
       model = Organisation
       fields = ('name', 'org_id')


class MembersSerializer(serializers.ModelSerializer):
   class Meta:
       model = Members
       fields = ('employee_id', 'email_id', 'first_name', 'last_name', 'middle_name', 'date_of_birth', 'gender')

class MembersAllSerializer(serializers.ModelSerializer):
    class Meta:
       model = Members
       fields = ('org_id','employee_id', 'email_id', 'first_name', 'last_name', 'middle_name', 'date_of_birth', 'gender')
 

class OrgMemeberSerializer(serializers.ModelSerializer):
    members = MembersSerializer(many=True, read_only=True)
    class Meta:
        model = Organisation
        fields = ['org_id', 'name', 'members']