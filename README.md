Installations

pip install django
pip install djangorestframework

Commands to run

python manage.py makemigrations
python manage.py migrate

python manage.py runserver

API endpoints, request body, responses

GET Organisations and members
endpoint: insurance/organisations/
![get_orgs_and_mems](https://user-images.githubusercontent.com/59283795/190856747-a2339cbe-6f8d-4aa3-beed-a665f32f2920.png)

POST Organisations
request body: {"items": [
    {
        "name": "plum",
        "org_id": 5
    },
    {
        "name": "inno",
        "org_id": 6
    }
]}
![post body](https://user-images.githubusercontent.com/59283795/190856858-adae2d62-e525-410e-8d0b-ad5bc6b0f669.png)
![post_data](https://user-images.githubusercontent.com/59283795/190856870-74490959-fec9-48a4-ba50-dbf5ff7701ff.png)


POST Members API
endpoint: insurance/organisations/<org_id>/members/
request body: { "items": [ { "employee_id": 4, "email": "haritha@gmail.com", "first_name": "Har", "last_name": "Kogara", "middle_name": "", "dob": "17/09/2000", "gender": "Female" }, { "employee_id": 5, "email": "harithakogara@gmail.com", "first_name": "HarithaR", "last_name": "Kogara", "middle_name": "", "dob": "17/09/2000", "gender": "Female" } ]}

get members

![members](https://user-images.githubusercontent.com/59283795/190856548-fe083471-fe44-4229-93f9-f6f14091108e.png)

post_members

![members_post](https://user-images.githubusercontent.com/59283795/190856525-d7e79b8c-ab3b-4d0c-ab10-886ab4c9b9b6.png)

invalid data

![invalid_members](https://user-images.githubusercontent.com/59283795/190857401-126297ec-945b-43c2-9173-9104f85d9ce5.png)
