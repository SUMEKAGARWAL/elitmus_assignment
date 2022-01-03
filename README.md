# elitmus_assignment
An advertising app with proper authentication and CRUD functionality using Django.

This assignment was basically intended to create a website such that the user can advertise their needs.
Features that were included in this web app:
1. User Flow:      

      a. Register
    
    
      b. Login
    
    
      c. Logout
      
2. Interface where user can


     a. Create Advertisement
     
     
     b. Publish Advertisement
     
     
     c. Edit Advertisement
     
     
     d. View Advertisement
     
     
     e. Delete Advertisement
     
3. Show All the published advertisement on the homepage for the web app

4. Registered users should be able to comment on Advertisements.

5. REST API-based architecture

For this project I have choosen SQLite("db.sqlite3") database which comes by defaukt with DJANGO REST framework application.
Uploaded Images are stored in this path : "/media/"

There were 5 HTML pages created and used for following purposes:

1. index.html : This is an Initial page where user will be landing as soon as he/she opens the website. Here he/she will be asked to register himself if he/she is not registered
                yet otherwise he/she can login into the website and work there after.
                
2. home.html : This page will be shown as soon as the user logs in. There are two buttons over here one named CREATE and second to LOGOUT. Also, all the advertisiments are shown 
               on this page after an user creates one at first. Comments and delete access is given to the registered user beneath each image.
    
3. create.html : In this page there are two inputs taken, one is the CAPTION and second is to choose the image from local system and upload and then PUBLISH.

4. Login.html and 5. Registration.html are for authenticating the user.


For any queries:
Mail to sumekagarwal123@gmail.com

               
