# # class Person:
# #     money = 100
#
# # user = Person()
#
# # print(user.money)
#
# # user1 = Person()
# # print(user1.money)
# # user.money = 200
#
# # print(user.money)
#
# # class Person:
# #     name = ''
# #     money = 0
#
#
# # person1 = Person()
# # person2 = Person()
#
# # person1.name = 'Erkin'
# # person2.name = 'Alibek'
#
# # person1.money = 100
# # person2.money = 50
#
# # print(person1.name, person1.money)
# # print(person2.name, person2.money)
#
#
# # class Person:
# #     name = ''
# #     money = 0
#
# #     def about(self):
# #         print(f"{self.name} has {self.money}")
#
# #     def change_money(self, new_money):
# #         self.money = new_money
#
# # person1 = Person()
#
# # person1.name = 'Erkin'
# # person1.about()
# # person1.change_money(200)
#
# # person1.about()
#
#
# # class Critter:
#
# #     total = 0
#
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #         Critter.total += 1
# #         print(f'Появилось новое животное {name}')
#
# #     def talk(self):
# #         print(f"hello. My name is {self.name}")
#
# #     @staticmethod
# #     def status():
# #         print(f"Сейчас всего {Critter.total} животных")
#
#
#
# # pet = Critter('Barbos', 4)
# # pet2 = Critter('Murzik', 2)
# # pet.talk()
# # Critter.status()
#
#
# # class A:
# #     def _private(self):
# #         print('This is private method')
#
# # a = A()
# # a._private()
#
# # class B:
# #     def __closed(self):
# #         print('This is closed method')
#
# #     def print_closed(self):
# #         self.__closed()
# #         print('closed method is working')
#
# # b = B()
# # b.print_closed()
#
#
# # class MyList(list):
#
#
# #     def my_method(self):
# #         print('My custom method')
#
# # list1 = MyList((1,2,3,4,5))
#
# # list1.append(10)
# # list1.insert(0, 1)
# # list1.insert(1, 2)
# # list1.insert(2, 3)
# # print(list1)
# # print(type(list1))
#
#
#
#
# # class Dog:
# #     total = 0
# #     def __init__(self, name, age, hunger=0):
# #         self.name = name
# #         self.age = age
# #         self.hunger = hunger
# #         Dog.total += 1
# #         print(f"created new object of class Dog")
# #         print(f"total objects of class {Dog.total}")
#
# #     def _pass_time(self):
# #         self.hunger += 1
#
# #     def talk(self):
# #         print(f"My name is {self.name}")
# #         self._pass_time()
#
# #     def eat(self):
# #         print("Thanks")
# #         self.hunger -= 2
# #         self._pass_time()
#
# #     def walk(self):
# #         print(f"i like to walk")
# #         self._pass_time()
#
# #     def status(self):
# #         print(f"hunger: {self.hunger}")
#
# # dog = Dog("Gray", 2, 3)
#
#
# # class Dachshund(Dog):
# #     # def _pass_time(self):
# #     #     self.hunger += 1
#
# #     def talk(self, text):
# #         print(text)
# #         self._pass_time()
#
# #     def sleep(self):
# #         print("Zzzzz")
# #         self._pass_time()
#
# # mini_dog = Dachshund('Dog', 3)
# # mini_dog.sleep()
# # mini_dog.eat()
# # mini_dog.talk('gav gav')
# # dog.talk()
# # dog.eat()
# # dog.status()
# # mini_dog.status()
#
# #
# # class Auto:
# #     def ride(self):
# #         print("Riding on a ground")
# #
# # class Boat:
# #     def swim(self):
# #         print("Sailing in the ocean")
# #
# # class Amphibian(Auto, Boat):
# #     pass
# #
# # a = Amphibian()
# #
# # a.swim()
# # a.ride()
#
# class MusicPlayerMixin:
#     def play_music(self, song):
#         print(f"Now playing: {song}")
#
#
# class Smartphone(MusicPlayerMixin):
#     pass
#
#
# class Radio(MusicPlayerMixin):
#     pass
#
#
# class Auto(MusicPlayerMixin):
#     pass
#
# a = Smartphone()
#
# a.play_music('lalala')
#
# b = Auto()
#
#
# b.play_music('lalala')
#
from pprint import pprint

x = "{'content_type': 'text', 'id': 203, 'message_id': 203, 'from_user': {'id': 959339948, 'is_bot': False, 'first_name': 'Erkin', 'username': 'err223', 'last_name': None, 'language_code': 'ru', 'can_join_groups': None, 'can_read_all_group_messages': None, 'supports_inline_queries': None}, 'date': 1614925498, 'chat': {'id': 959339948, 'type': 'private', 'title': None, 'username': 'err223', 'first_name': 'Erkin', 'last_name': None, 'photo': None, 'bio': None, 'description': None, 'invite_link': None, 'pinned_message': None, 'permissions': None, 'slow_mode_delay': None, 'sticker_set_name': None, 'can_set_sticker_set': None, 'linked_chat_id': None, 'location': None}, 'forward_from': None, 'forward_from_chat': None, 'forward_from_message_id': None, 'forward_signature': None, 'forward_sender_name': None, 'forward_date': None, 'reply_to_message': None, 'edit_date': None, 'media_group_id': None, 'author_signature': None, 'text': '/start', 'entities': [<telebot.types.MessageEntity object at 0x7f82473e8ee0>], 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'animation': None, 'dice': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'reply_markup': None, 'json': {'message_id': 203, 'from': {'id': 959339948, 'is_bot': False, 'first_name': 'Erkin', 'username': 'err223', 'language_code': 'ru'}, 'chat': {'id': 959339948, 'first_name': 'Erkin', 'username': 'err223', 'type': 'private'}, 'date': 1614925498, 'text': '/start', 'entities': [{'offset': 0, 'length': 6, 'type': 'bot_command'}]}}"
pprint(x)