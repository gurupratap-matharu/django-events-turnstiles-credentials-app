# A django app to handle access to various to events.

A django projects that registers events, turnstiles, credentials for
various types of projects.

It allows users to

* create events
* create turnstiles(molinetes) and connect them to events
* create credentials(access card) and register them with turnstiles
* see credentials registered for a particular event
* see credentials registered for a particular turnstile
* delete all of the above
* a django admin interface for registering users and giving access permissions

Event have a

* Creation date
* title
* Id / code

Turnstiles and Credentials have a

* identification code or number
* creation and updation date
* credentials in particular have a read status


The interface itself permits

* To register a new events, turnstiles and credentials.
* Validation is supported on all of the above.

## License

This code is open source. So feel free to use, modify, share, download as per your need. I do not take risk nor responsibility for your errors or any commercial damage.

## How to run?

This code is written in python3.7

## On local machine

Go to the mysite project folder that contains the manage.py file and then
```
python manage.py runserver
```

Else directly access the webapp on this link
