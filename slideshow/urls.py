from django.conf.urls import patterns, include, url
from views import hidden_data, load_list_all,load_list, cath_to_save_list ,approving_simple, tree, login, text, test2, current_datetime, hours_ahead, search_form, search, contact, test, slideshow9, img1, approving, test1, approving_full
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	('^time/$', current_datetime),
	('^time/plus/(\d{1,2})/$', hours_ahead),
	(r'^search-form/$', search_form),
	(r'^search/$', search),
	(r'^contact-form/$', contact),
	(r'^test/$', test),
	(r'^slideshow9/$', slideshow9),
	(r'^img1/$', img1),
	(r'^approving_full/$', approving_full),
	(r'^approving/$', approving),
	(r'^approving-s/$', approving_simple),
	(r'^test1/$', test1),
	(r'^test2/$', test2),
	(r'^approving_full/text$', text),
	(r'^approving_full/cath_to_save_list$', cath_to_save_list),
	(r'^approving_full/load$', load_list),
	(r'^approving_full/load-all$', load_list_all),
	(r'^approving_full/hidden-data$', hidden_data),
	(r'login/$', login),
	(r'tree/$', tree),
	

	(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'slideshow.views.home', name='home'),
    # url(r'^slideshow/', include('slideshow.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
