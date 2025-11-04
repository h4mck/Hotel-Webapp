from django import template
from wagtail.models import Site, Page

register = template.Library()

@register.simple_tag(takes_context=True)
def get_site_root(context):
    # This returns a core.Page. The main menu needs to have the site.root_page
    # defined else will return an object attribute error ('str' object has no
    # attribute 'get_children')
    return Site.find_for_request(context["request"]).root_page

# Retrieves the top menu items - the immediate children of the parent page
@register.inclusion_tag("tags/top_menu.html", takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    # for menuitem in menuitems:
    #     # We don't directly check if calling_page is None since the template
    #     # engine can pass an empty string to calling_page
    #     # if the variable passed as calling_page does not exist.
    #     menuitem.active = (
    #         calling_page.url_path.startswith(menuitem.url_path)
    #         if calling_page
    #         else False
    #     )
    return {
        # "calling_page": calling_page,
        "menuitems": menuitems,
        # required by the pageurl tag that we want to use within this template
        "request": context["request"],
    }

@register.inclusion_tag("tags/breadcrumbs.html", takes_context=True)
def breadcrumbs(context):
    self = context.get("self")
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(self, inclusive=True).filter(depth__gt=1)
    return {
        "ancestors": ancestors,
        "request": context["request"],
    }