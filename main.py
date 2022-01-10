#I can make it a dropdown on the navbar
#I think I can make a log in
#What sid said I think I can make it startup on command
#Submitted messahe
#Where to display error messages



from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
