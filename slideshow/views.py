import MySQLdb, sys, os, random

# sys.path.append("/home/russel/djcode/slideshow/")
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext

from django.core.mail import send_mail
from django.http import HttpResponseRedirect

from model.models import Twitters, Garbage, Lists
from django.contrib.auth.models import User
import ldap


database = Twitters.objects.all()
data_selected = []
urls = []

def current_datetime(request):
    now = datetime.datetime.now()
    author = Author.objects.filter(first_name='1')
    return render_to_response('extend_file.html', 
    						  {'current_date': now, 'path':request.get_host(), 
    						   'is_sec':request.is_secure(), 
    						   'user_info':request.META['HTTP_USER_AGENT'],
    						   'author':'hi' })


def test(request):   
    f = open('/home/russel/tmp/sourse_file.txt', 'r')
    k = f.readlines()
    for i in k:
        value1 = i
    f.close()

    return render_to_response('test.html', {'value1':value1})
 


def hours_ahead(request, offset):
    try:
    	offset = int(offset)
    except ValueError:
    	raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html', {'hour_offset': offset, 'next_time':dt})


def search_form(request):
	return render_to_response('search_form.html', {'error': False})


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
        	errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q})
    return render_to_response('search_form.html',
        {'errors': errors})

def contact(request):
    errors = []
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
    	form = ContactForm(
    		initial={'subject':"I love your site!"})
    return render_to_response('contact_form.html', {'form': form})

def slideshow9(request):
    # global database
    # global data_selected
    global urls 
    a = request.session['urls']
    # print urls
    value_dict = {}
    # print a.keys()
    key = 1
    
    for i in range(9):
        value_dict['img'+str(key)] = random.choice(a)
        key += 1
    return render_to_response('test.html', value_dict)

def img1(request):
    # global database
    # global data_selected
    global urls
    # print data_selected
    # for i in database:
    #     if i.aprove==1:
    #         data_selected.append(i)
    value_dict={'img1':random.choice(request.session['urls'])}
    return render_to_response('1img.html', value_dict)


from django.template import Template, Context

from django.http import HttpResponse

# -------------------------------------------------------------------------------------------------------
# FOR Approving 

def approving(request):
    global data_selected
    global urls
    urls = read_from_database_all()
    value_dict = {}
    url_template =  """<li id="{{ key }}" class="ui-widget-content ui-corner-tr">
        <h5 class="ui-widget-header">Image {{ key }}</h5>
        <img src={{ urls }} alt="Photo {{key}}" width="96" height="72" />
        <a href={{ urls }} title="View larger image" class="ui-icon ui-icon-zoomin">View larger</a>
        <a href="link/to/trash/script/when/we/have/js/off" title="Delete this image" class="ui-icon ui-icon-trash">Delete image</a>
    </li> """
    t = Template(url_template)
    url_concat = ''
    part1, part2 = '', ''
    # key = 1                 
    for key, photo in urls.iteritems():
        url_concat += t.render(Context({'key':key, 'urls':photo}))
        # key+=1
    # url_concat += """<button type="submit" onClick="pushButton()"> Act </button>"""
    return HttpResponse(url_concat)

# its bad versio for that momment
def approving_simple(request):
    global data_selected
    global urls
    urls = read_from_database_all()
    value_dict = {}
    url_template =  """<li id="{{ key }}" class="ui-widget-content ui-corner-tr">
        <h5 class="ui-widget-header">Image {{ key }}</h5>
        <img src={{ urls }} alt="Photo {{key}}" width="96" height="72" />
        <a href={{ urls }} title="View larger image" class="ui-icon ui-icon-zoomin">View larger</a>
        <a href="link/to/trash/script/when/we/have/js/off" title="Delete this image" class="ui-icon ui-icon-trash">Delete image</a>
    </li> """
    t = Template(url_template)
    url_concat = ''
    part1, part2 = '', ''
    key = 1                 
    for photo in urls:
        url_concat += t.render(Context({'key':key, 'urls':photo}))
        key+=1

    return HttpResponse(urls)
    
def approving_full(request):
    global database
    global data_selected
    data_selected = []
    if request.POST:
        print "There is POST"
    if request.GET:
        print "There is GET"
    print request.session['name']
     


    return render_to_response('approve.html')
    
    


def read_from_database_all():
    global database
    global urls

    urls = {}
    for i in database:
        if i.img!=None:
            urls[i.id]=i.img
    return urls

def test1(request):
    return render_to_response('mouse.html')

def test2(request):
    return render_to_response('dnd.html')

def text(request):
    global data_selected
    global urls
    tmp = 0
    if request.POST:
        print "There is POST"
    if request.GET:
        print "There is GET"

    for key, value in request.POST.iteritems():
        p = Twitters.objects.get(img=value)
        request.session[p.id]=p.img
    if 'a0' in request.POST:
        print "There are a0"
    global database
    urls = request.session.values()
    print urls
    for i in database:
        if i.aprove==1:
            data_selected.append(i)


def login(request):
    global urls
    urls = []
    errors = []
    login = ''
    password = ''
    username = ''
    request.session.clear()
    server = 'ldap://172.22.64.41:389'

    base_dn='ou=Technical,dc=nc,dc=local'

    if 'login' in request.POST:
        user = request.POST['login']
        username = r"nc.local\%s" % user
        if not user:
            errors.append('It seems to be no login was entered')
    if 'password' in request.POST:
        password = request.POST['password']
        if not password:
            errors.append('It seems to be no password was entered')

    if len(errors) == 0 and 'login' in request.POST and 'password' in request.POST:    
        l = ldap.initialize(server)
        l.protocol_version = 3
        try :
            l.simple_bind_s(username,password)
            searchFilter = "cn=*"
            retrieveAttributes = ['cn']
            results = l.search_s(base_dn,ldap.SCOPE_SUBTREE,searchFilter, retrieveAttributes)
            errors.append("Access granded")
            print request.session.values()
            print urls
            request.session['name'] = request.POST['login']
            return redirect('/approving_full')
        except ldap.LDAPError:
            errors.append("Permission denied by Active Directory")

    return render_to_response('login.html',
        {'errors': errors})


def tree(request):
    return render_to_response('tree.html', {}, context_instance=RequestContext(request))

def cath_to_save_list(request):
    if request.POST:
        print "There is POST"
    if request.GET:
        print "There is GET"
    massive = ''
    list_name=''
    for key, value in request.POST.iteritems():
        if (key=="list_name"):
            list_name = value
        if (key=="name"):
            request.session[key] = value;
            # print request.session[key]
    for key, value in request.POST.iteritems():
        print ("key:%s, value:%s" %(key, value))
        massive += "key:%s, value:%s" %(key, value)
        if (key[:4]=="item"):
            a = Lists(user="rmalogulko",
                list_id=list_name,
                url=value)
            a.save()
        print list_name



    return HttpResponse(massive)

def load_list(request):
    all_items = Lists.objects.all()
    unique = []
    for i in all_items:
        if i.list_id not in unique:
            unique.append(i.list_id)
    print unique
    a = ''
    for i in unique:
        a += '<li class="ui-widget-content">'+ i +'</li>'
    a += '<p>Last selected list to load</p>'
    a += '<li id="last-selected" class="ui-widget-content">'+request.session['name']+'</li>'
    return HttpResponse(a)

def load_list_all(request):
    return render_to_response('load_list.html')

def hidden_data(request):
    var = Lists.objects.filter(list_id=request.session["name"])
    ids_to_delete = []
    for i in database:
        for j in var:
            if (j.url==i.img):
                ids_to_delete.append(str(i.id)+"del")

    to_trash = ''
    url_to_session = []
    iterate = 0;
    for i in var:
        to_trash += '<p id=' + str(ids_to_delete[iterate]) + '>' + i.url + '</p>'
        url_to_session.append(i.url)
        iterate+=1
    print to_trash
    request.session['urls'] = url_to_session
    return HttpResponse(to_trash)




