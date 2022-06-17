# e-commerce-site1


# static css file for styling
1. create style.css file in static > 'appname' > style.css > add styling.
2. add the code  - > {% load static %} at the top
3. add the code  - > <link rel="stylesheet" href="{% static 'app1/styles.css' %}">

# Tailwind
npm init -y
# install in the app & project dir
npm install tailwindcss@2.2.16
# Compile
1. Create folder in static > 'appname' > src folder > tw.css
2. add @tailwind base; @tailwind components; @tailwind utilities; to tw.css file
3. Go to package.json > script > add this line {k:v} > example: "build": "tailwind  build app1/static/app1/src/tw.css -o app1/static/app1/styles.css"
4. open terminal and type - 'npm run build'


# Setting the media root for images
1. visit settings.py > add the line at the end ->   
    MEDIA_ROOT = BASE_DIR / 'media'
    MEDIA_URL = '/media/'
2. visit urls.py (main project folder)  add the lines-> 
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
