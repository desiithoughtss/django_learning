from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

posts=[
    {
    "id": 1,
    "title":"python",
    "content": "this is the python programming language"
},
{
    "id": 2,
    "title":"javascript",
    "content": "this is the javascript programming language"  
},
{
    "id": 3,
    "title":"django",
    "content": "this is the djangos programming language"  
}
]

# Create your views here.

def home(request, name):
    html = ""
    for post in posts:
        html += f"""
        <div> 
        <a href="/posts/{post["id"]}"><h1>{post["id"]} - {post["title"]}</h1></a>
        <p>{post["content"]}</p>
        </div>
        """
    return HttpResponse(html)


def post(request, id):
    valid_response = False
    for post in posts:
        if post["id"] == id:
            post_dict = post
            valid_response = True
            break
    if valid_response:
        html = f"""
            <div>
            <h1>{post_dict["title"]}</h1>
            <p> {post_dict["content"]}</p>
            </div>
            """
        return HttpResponse(html)
    else:
        return HttpResponseNotFound("response not found")


def google(request):
    return HttpResponseRedirect("https://www.google.com")

def onlyID(request, id):
    return HttpResponseRedirect(f"/posts/{id}/")

    
def home_page(request):
    return HttpResponse("This is the homepage")

def template_home(request):
    name = "akshit"
    # return render(request, "posts/home.html", {"name": name, "list":["a"]})
    return render(request, "posts/home.html", {"posts": posts})