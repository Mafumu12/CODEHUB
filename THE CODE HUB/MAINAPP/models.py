from django.db import models
from PROFILEAPP.models import UserProfile
# Create your models here.




class List_Of_Friends(models.Model):
    friend = models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name='friend')
    friends = models.ManyToManyField(UserProfile, blank=True,related_name='friends')

    def __str__(self):
       return self.friend.username
    
    def add_friend(self,account):

        if account not in self.friends.all():
            self.friends.add(account)

    def remove_friend(self,account):

        if account in self.friends.all():
            self.friends.remove(account)

    def unfriend(self, removee):
        remover = self
        remover.remove_friend(removee)
        Friend_List = List_Of_Friends.objects.get(friend = removee)
        Friend_List.remove_friend(self.friend)

    def mutal_friend(self,name):

        if name in self.friends.all():
            return True
        return False


class FriendRequest(models.Model):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name= "sender")
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name= "receiver")
    is_active = models.BooleanField(blank=True, null=False, default=True)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username
    
    def accept(self):
        receiver_friend_list = List_Of_Friends.objects.get(friend = self.receiver)
        if receiver_friend_list:
            receiver_friend_list.add_friend(self.sender)
            sender_friend_list = List_Of_Friends.objects.get(firend= self.sender)
            if sender_friend_list:
                sender_friend_list.add_friend(self.receiver)
                self.is_active = False
                self.save()


    def decline(self):
        self.is_active = False
        self.save()

    def cancel(self):
        self.is_active = False
        self.save()