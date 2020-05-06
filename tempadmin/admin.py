from django.contrib.admin.sites import AdminSite
from django.views.decorators.cache import never_cache
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import gettext as _
from .forms import UserAdminAuthenticationForm


class UserAdmin(AdminSite):
    # Anything we wish to add or override

    login_form = UserAdminAuthenticationForm

    def has_permission(self, request):
        """
        Removed check for is_staff.
        """
        return request.user.is_active

    @never_cache
    def login(self, request, extra_context=None):
        """
        Display the login form for the given HttpRequest.
        """
        if request.method == 'GET' and self.has_permission(request):
            # Already logged-in, redirect to admin index
            index_path = reverse('admin:index', current_app=self.name)
            return HttpResponseRedirect(index_path)

        from django.contrib.auth.views import LoginView
        # Since this module gets imported in the application's root package,
        # it cannot import models from other applications at the module level,
        # and django.contrib.admin.forms eventually imports User.
        # from django.contrib.admin.forms import UserAdminAuthenticationForm
        context = {
            **self.each_context(request),
            'title': _('Log in'),
            'app_path': request.get_full_path(),
            'username': request.user.get_username(),
        }
        if (REDIRECT_FIELD_NAME not in request.GET and
                REDIRECT_FIELD_NAME not in request.POST):
            context[REDIRECT_FIELD_NAME] = reverse('admin:index',
                                                   current_app=self.name)
        context.update(extra_context or {})

        defaults = {
            'extra_context': context,
            'authentication_form': self.login_form or
            UserAdminAuthenticationForm,
            'template_name': self.login_template or 'admin/login.html',
        }
        request.current_app = self.name
        return LoginView.as_view(**defaults)(request)


user_admin_site = UserAdmin(name='usersadmin')

# Run user_admin_site.register() for each model we wish to register
# for our admin interface for users


# Run admin.site.register() for each model we wish to register
# with the REAL django admin!
