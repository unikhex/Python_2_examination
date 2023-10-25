# Python_2_examination

Individual examination excerise for python 2 at DevOps-2023 (nackademin)

## A basic idea of what the endproduct should contain

 A flask app that has a front-end(HTML in this case)

The app should have a form that inputs:

- Year
- Month
- Day
- priceclass (using an API that e have been given)

Th form should limit for choosing only a day in the future while at the same time, only go back to 2022-11-01. Anything else should turnout to an error message.

The form should then be sent usng the POSt method to my own endpoint.