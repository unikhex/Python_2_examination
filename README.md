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

## Version changes

To here i'll call it version 1

The basics have been done. Meaning:

- Html pages set up.
- The api code is written but non-functioning due to server issues.
- Flask working as intended and all modeles that are required set up.

What i plan on adding is:

- Add stuff to the HTML pages as they are pretty much blank currently.(Functionality and such)
- Adding restrictions on which dates can be chosen and how far back we can go.

It currently looks like this.

Index page(Main page)

(![Main page](/examination/application/static/image.png))

Form Page

![Form page](/examination/application/static/image-1.png)

## Problems encountered with this version

The server couldn't end the needed information. But this is most likely a problem with my coding not the server. Will be fixed later. It looks like:

![Problem encountered](/examination/application/static/image-2.png)
