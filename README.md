# PetCare

PetCare is a django based animal help portal that helps you locate vets and health services for your pets. Check it out live in use [here] (https://pet-care.herokuapp.com/)

## Installation:
Ensure that you have Python 2.7 installed along with Django 1.8. You would also need to install Python [googlemaps library](https://pypi.python.org/pypi/googlemaps/). You can do this through the following command:


    pip install -U googlemaps

Once, you have all the requirements, you can `clone` the project into your workplace as follows:

    git clone https://github.com/Famguy/PetCare.git

You would also have to get a working Google Maps API key. More about it can be found [here] (https://developers.google.com/maps/documentation/javascript/get-api-key). The app contains a temporary key that was used for testing.

## Running the app:
Once you have the repository cloned into your system, you can quickly run it with the following commands:


    cd working-directory/PetCare/petcare
    python manage.py syncdb
    python manage.py runserver








