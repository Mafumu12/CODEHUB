from django.contrib import admin

from .models import FriendRequest,List_Of_Friends


class ListOfFriendsAdmin(admin.ModelAdmin):
    list_filter =['friend']
    list_display = ['friend']
    search_fields = ['friend']
    readonly_fields = ['friend']

    class Meta:
        model = List_Of_Friends


admin.site.register(List_Of_Friends,ListOfFriendsAdmin)

class FreindRequestAdmin(admin.ModelAdmin):
    list_filter =['sender','receiver']
    list_display = ['sender','receiver']
    search_fields = ['sender__username','receiver__username']
    

    class Meta:
        model = FriendRequest


admin.site.register(FriendRequest,FreindRequestAdmin)



# Register your models here.
