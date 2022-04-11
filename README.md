This project required me to create an application that will use a CRUD Functionalty that will allow the user to manage a Book Library.

- Project Management Tools - Jira Kanban Board and Github.
- Databases - mySQL
- Backend Application - Flask
- Front End - HTML
- Testing - Unit testing Python (Backend) PostMan(FrontEnd)
- Cloud - Google Cloud Platform
- Build Server - Jenkins


```
- The user will be able to create, update, delete, view all books in the system.
```

A Flask application will react with a MySQL Database, HTML to create a fully functioning application that will be connected to a virutal environment and be able to do the do the following

```
- CREATE books
- VIEW all books
- UPDATE books
- DELETE books
- CREATE reviews
- VIEW reviews
- UPDATE views
- DELETE views
```

## Application Planning Stages.

Project Management tool Jira was used to plan this project.
Epics were created to outline what tasks were needed for completion this was based on project specifications outlined by QA Trainers and was completed in a one week sprint.


![image](https://user-images.githubusercontent.com/98025347/162742593-48db66f2-8ad3-4734-9632-1d8b1f556631.png)




### Creation of DataBases

mySQL was used as databases and was connected through an virtual environment on the google cloud platform

![image](https://user-images.githubusercontent.com/98025347/162745966-3936fc7a-f1fd-4ec8-8d81-9320a24b9324.png)


mySQL was used to create databases and viewed creation through workbench mySQL

![image](https://user-images.githubusercontent.com/98025347/162746657-f5fcc858-5643-4f7f-a4e8-2d7dc158ebaf.png)
![image](https://user-images.githubusercontent.com/98025347/162746734-19930bfd-e73a-4395-95d4-64a30eb4f61c.png)

## Flask BackEnd Creation

Visual Studio Code was created a flask project, a class was created for routes, models and templates folder for HTML

``` Routes ```
![image](https://user-images.githubusercontent.com/98025347/162748209-655280a8-f02d-49c9-a58f-21ecc16187e0.png)


``` Models ```
![image](https://user-images.githubusercontent.com/98025347/162748288-e6420328-062d-4e50-b0b8-da99bead8bab.png)

``` html ```
![image](https://user-images.githubusercontent.com/98025347/162748444-42ff9530-8238-4d65-baaa-4162df979e87.png)

### Unit Tests 
pytests Testing was used for this project with an overall coverage of 86.%, 102 lines of code were tested and 14 were untested, due to time constraints. I firsted tested the end point responses to my routes, with the aim of recieving a status_code 200, these were to ensure all end points and routes were correctley functioning.

Moreover, this followed by testing on a "db.create" which essentially would create a database and check for the attributes i assigned (as seen below). Futhermore I deeper tested the routes and was able to test all create, read and update methods in the application

![image](https://user-images.githubusercontent.com/98025347/162749475-f4b5e00d-e0b5-4fb3-9af3-551304cb303f.png)


## FrontEnd Creation

FrontEnd was created through simplistic html designs - the purpose of this project was to create a CRUD and utilise, the python language and be able to main a hosted virtual environment, so very little styling was done, however the navigation bar can be attributed to the bootstrap website as this was a template for public viewing - https://getbootstrap.com/docs/4.0/components/navbar/

The crud functionality was succesfully created and implemented

![image](https://user-images.githubusercontent.com/98025347/162750345-b4b4d166-cec9-4cb1-9e75-6728a65602ba.png)
![image](https://user-images.githubusercontent.com/98025347/162750420-b1a5144f-ab4d-4e9d-a6e4-547e8f81dc60.png)
![image](https://user-images.githubusercontent.com/98025347/162750499-44b67a88-dd70-44b0-9754-d78ab96120f4.png)
![image](https://user-images.githubusercontent.com/98025347/162750771-c19de2b4-76cd-48c1-9bd2-24629ef58825.png)



