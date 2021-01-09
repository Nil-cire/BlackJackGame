import kivy
import random
from random import sample
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.graphics import Color, Rectangle


class BlackJackTable(FloatLayout):
    def __init__(self, **kwargs):
        super(BlackJackTable, self).__init__(**kwargs)
        ### Widgets

        self.display_size = (0.4, 0.2)
        self.display_pos_x = 0.05
        self.display_pos_y = 0.8
        self.new_game_button_size = (0.15, 0.1)
        self.new_game_button_pos_x = 0.8
        self.new_game_button_pos_y = 0.85
        self.call_card_size = (0.15, 0.1)
        self.call_card_pos_x = 0.625
        self.call_card_pos_y = 0.85
        self.stop_call_size = (0.15, 0.1)
        self.stop_call_pos_x = 0.45
        self.stop_call_pos_y = 0.85
        self.house_label_size = (0.9, 0.3)
        self.house_label_pos_x = 0.05
        self.house_label_pos_y = 0.45
        self.player_label_size_x = 0.9
        self.player_label_size_y = 0.3
        self.player_label_pos_x = 0.05
        self.player_label_pos_y = 0.05
        self.house_zone_color = (0.3, 1, 0)
        self.player_zone_color = (0.3, 1, 0)
        self.card_size = (0.12, 0.25)
        self.player_card_pos_x = 0.075
        self.player_card_pos_y = 0.075
        self.house_card_pos_x = 0.075
        self.house_card_pos_y = 0.475

        self.card_list_total = None
        self.card_sum = 0
        self.card_amount_list = []
        self.house_sum = 0
        self.house_sum_list =[]


        ### Cards Value
        self.hc1 = 0
        self.hc2 = 0
        self.hc3 = 0
        self.hc4 = 0
        self.hc5 = 0
        self.hc6 = 0

        self.pc1 = 0
        self.pc2 = 0
        self.pc3 = 0
        self.pc4 = 0
        self.pc5 = 0
        self.pc6 = 0


        ### Board widget
        self.display = Label(text="Welcome to the game!",
                             font_size=30,
                             size_hint=self.display_size,
                             pos_hint={"x": self.display_pos_x, "y": self.display_pos_y})
        self.player_zone = Button(text="Player",
                                  size_hint=(self.player_label_size_x, self.player_label_size_y),
                                  pos_hint={"x": self.player_label_pos_x, "y": self.player_label_pos_y},
                                  color=(0, 0, 1, 1),
                                  background_color=[1, 1, 0, 1])
        self.player_zone.disabled = True
        self.house_zone = Button(text="Host",
                                 size_hint=self.house_label_size,
                                 pos_hint={"x": self.house_label_pos_x, "y": self.house_label_pos_y},
                                 background_color=[1, 1, 0, 1])
        self.house_zone.disabled = True

        self.add_widget(self.player_zone)
        self.add_widget(self.house_zone)
        self.add_widget(self.display)
        #New game button
        self.new_game = Button(text="New game",
                               size_hint=self.new_game_button_size,
                               pos_hint={"x": self.new_game_button_pos_x, "y": self.new_game_button_pos_y})
        self.new_game.bind(on_release=self.start_cards)
        self.add_widget(self.new_game)
        #Call card button
        self.call_card = Button(text="Call a card!",
                                size_hint=self.call_card_size,
                                pos_hint={"x": self.call_card_pos_x, "y": self.call_card_pos_y})
        self.call_card.bind(on_release=self.call_a_card)
        self.add_widget(self.call_card)
        ###Stop call(Dual!)
        self.stop_call = Button(text="Stop",
                                size_hint=self.stop_call_size,
                                pos_hint={"x": self.stop_call_pos_x, "y":self.stop_call_pos_y})
        self.stop_call.bind(on_release=self.deal)
        self.add_widget(self.stop_call)
        #house New cards (Button)
        self.house_card2_cover = Button(text="",
                                        size_hint=self.card_size,
                                        pos_hint={"x": self.house_card_pos_x + 0.14166, "y": self.house_card_pos_y})

        self.house_card1 = Button(text="",
                                  size_hint=self.card_size,
                                  pos_hint={"x": self.house_card_pos_x, "y": self.house_card_pos_y})

        self.house_card2 = Button(text="",
                                  size_hint=self.card_size,
                                  pos_hint={"x": self.house_card_pos_x + 0.14166, "y": self.house_card_pos_y})

        self.house_card3 = Button(text="",
                                  size_hint=self.card_size,
                                  pos_hint={"x": self.house_card_pos_x + 0.14166 * 2, "y": self.house_card_pos_y})

        self.house_card4 = Button(text="",
                                  size_hint=self.card_size,
                                  pos_hint={"x": self.house_card_pos_x + 0.14166 * 3, "y": self.house_card_pos_y})

        self.house_card5 = Button(text="",
                                  size_hint=self.card_size,
                                  pos_hint={"x": self.house_card_pos_x + 0.14166 * 4, "y": self.house_card_pos_y})

        self.house_card6 = Button(text="",
                                  size_hint=self.card_size,
                                  pos_hint={"x": self.house_card_pos_x + 0.14166 * 5, "y": self.house_card_pos_y})
        ##player card button
        self.player_card1 = Button(text="",
                                   size_hint=self.card_size,
                                   pos_hint={"x": self.player_card_pos_x, "y": self.player_card_pos_y})

        self.player_card2 = Button(text="",
                                   size_hint=self.card_size,
                                   pos_hint={"x": self.player_card_pos_x + 0.14166, "y": self.player_card_pos_y})

        self.player_card3 = Button(text="",
                                   size_hint=self.card_size,
                                   pos_hint={"x": self.player_card_pos_x + 0.14166 * 2, "y": self.player_card_pos_y})

        self.player_card4 = Button(text="",
                                   size_hint=self.card_size,
                                   pos_hint={"x": self.player_card_pos_x + 0.14166 * 3, "y": self.player_card_pos_y})

        self.player_card5 = Button(text="",
                                   size_hint=self.card_size,
                                   pos_hint={"x": self.player_card_pos_x + 0.14166 * 4, "y": self.player_card_pos_y})

        self.player_card6 = Button(text="",
                                   size_hint=self.card_size,
                                   pos_hint={"x": self.player_card_pos_x + 0.14166 * 5, "y": self.player_card_pos_y})

    def start_cards(self, instance):
        ###Clearing old widgets

        self.call_card.disabled = False
        self.display.text = "Welcome to the game!"
        self.widget_list = [self.house_card1, self.house_card2, self.house_card3, self.house_card4, self.house_card5,
                            self.house_card6, self.player_card1, self.player_card2, self.player_card3,
                            self.player_card4, self.player_card5, self.player_card6, self.house_card2_cover]
        for widget in self.widget_list:
            if isinstance(widget, Button):
                self.remove_widget(widget)
        self.player_card3.text = ""
        self.player_card4.text = ""
        self.player_card5.text = ""
        self.player_card6.text = ""
        #Resetting values
        self.card_sum = 0
        self.house_sum = 0
        self.pc1 = 0
        self.pc2 = 0
        self.pc3 = 0
        self.pc4 = 0
        self.pc5 = 0
        self.pc6 = 0
        self.hc1 = 0
        self.hc2 = 0
        self.hc3 = 0
        self.hc4 = 0
        self.hc5 = 0
        self.hc6 = 0


        #Card Deck
        self.card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.card_list_total = self.card_list * 4

        self.add_widget(self.player_card1)
        self.add_widget(self.player_card2)
        self.add_widget(self.house_card1)
        self.add_widget(self.house_card2)
        self.add_widget(self.house_card2_cover)

        #player picking cards
        p_c_1 = sample(self.card_list_total, 1)
        for i in p_c_1:
            self.card_list_total.remove(i)
            self.player_card1.text = str(i)
        p_c_2 = sample(self.card_list_total, 1)
        for i in p_c_2:
            self.card_list_total.remove(i)
            self.player_card2.text = str(i)
            ####Showing sum of hand card
        if self.player_card1.text == "":
            self.pc1 += 0
        elif self.player_card1.text != "":
            if self.player_card1.text in ("11", "12", "13"):
                self.pc1 += 10
            elif self.player_card1.text == "1":
                self.pc1 += 11
            else:
                self.pc1 += int(self.player_card1.text)

        if self.player_card2.text == "":
            self.pc2 += 0
        elif self.player_card2.text != "":
            if self.player_card2.text in ("11", "12", "13"):
                self.pc2 += 10
            elif self.player_card2.text == "1":
                self.pc2 += 11
            else:
                self.pc2 += int(self.player_card2.text)

        player_a_check = 0
        player_start_list = [self.pc1, self.pc2]
        for p in player_start_list:
            if p == 11:
                player_a_check += 1
        player_start_sum = self.pc1 + self.pc2
        if player_start_sum > 21:
            if player_a_check > 0:
                player_start_sum -= 10
        self.card_sum = player_start_sum

        self.display.text = str(player_start_sum)
        ###host picking card
        h_c_1 = sample(self.card_list_total, 1)
        for i in h_c_1:
            self.card_list_total.remove(i)
            self.house_card1.text = str(i)
            hc1 = i

        h_c_2 = sample(self.card_list_total, 1)
        for i in h_c_2:
            self.card_list_total.remove(i)
            self.house_card2.text = str(i)
            self.house_card2.disabled = True
            hc2 = i

    def call_a_card(self, instance):
        if self.card_list_total == None:
            print("Please start a new game")
        elif self.card_list_total != None:
            if self.player_card3.text == "":
                self.add_widget(self.player_card3)
                p_c_3 = sample(self.card_list_total, 1)
                for i in p_c_3:
                    self.card_list_total.remove(i)
                    self.player_card3.text = str(i)
            elif self.player_card3.text != "":
                if self.player_card4.text == "":
                    self.add_widget(self.player_card4)
                    p_c_4 = sample(self.card_list_total, 1)
                    for i in p_c_4:
                        self.card_list_total.remove(i)
                        self.player_card4.text = str(i)
                elif self.player_card4.text != "":
                    if self.player_card5.text == "":
                        self.add_widget(self.player_card5)
                        p_c_5 = sample(self.card_list_total, 1)
                        for i in p_c_5:
                            self.card_list_total.remove(i)
                            self.player_card5.text = str(i)
                    elif self.player_card5.text != "":
                        if self.player_card6.text == "":
                            self.add_widget(self.player_card6)
                            p_c_6 = sample(self.card_list_total, 1)
                            for i in p_c_6:
                                self.card_list_total.remove(i)
                                self.player_card6.text = str(i)
                        elif self.player_card6.text != "":
                            print("No more cards!")

        return self.result_check()

    def result_check(self):
        #### define card value
        self.pc1 = 0
        self.pc2 = 0
        self.pc3 = 0
        self.pc4 = 0
        self.pc5 = 0
        self.pc6 = 0
        if self.player_card1.text == "":
            self.pc1 += 0
        elif self.player_card1.text != "":
            if self.player_card1.text in ("11", "12", "13"):
                self.pc1 += 10
            elif self.player_card1.text == "1":
                self.pc1 += 11
            else:
                self.pc1 += int(self.player_card1.text)

        if self.player_card2.text == "":
            self.pc2 += 0
        elif self.player_card2.text != "":
            if self.player_card2.text in ("11", "12", "13"):
                self.pc2 += 10
            elif self.player_card2.text == "1":
                self.pc2 += 11
            else:
                self.pc2 += int(self.player_card2.text)

        if self.player_card3.text == "":
            self.pc3 += 0
        elif self.player_card3.text != "":
            if self.player_card3.text in ("11", "12", "13"):
                self.pc3 += 10
            elif self.player_card3.text == "1":
                self.pc3 += 11
            else:
                self.pc3 += int(self.player_card3.text)

        if self.player_card4.text == "":
            self.pc4 += 0
        elif self.player_card4.text != "":
            if self.player_card4.text in ("11", "12", "13"):
                self.pc4 += 10
            elif self.player_card4.text == "1":
                self.pc4 += 11
            else:
                self.pc4 += int(self.player_card4.text)

        if self.player_card5.text == "":
            self.pc5 += 0
        elif self.player_card5.text != "":
            if self.player_card5.text in ("11", "12", "13"):
                self.pc5 += 10
            elif self.player_card5.text == "1":
                self.pc5 += 11
            else:
                self.pc5 = int(self.player_card5.text)

        if self.player_card6.text == "":
            self.pc6 += 0
        elif self.player_card6.text != "":
            if self.player_card6.text in ("11", "12", "13"):
                self.pc6 += 10
            elif self.player_card6.text == "1":
                self.pc6 += 11
            else:
                self.pc6 += int(self.player_card6.text)

        print(self.pc1)
        print(self.pc2)
        print(self.pc3)
        self.display.text = self.player_card3.text

         ###sum up hand cards
        self.card_sum_list = [self.pc1, self.pc2, self.pc3, self.pc4, self.pc5, self.pc6]
        self.card_sum = 0
        print(self.card_sum_list)
        for i in self.card_sum_list:
            self.card_sum += i
        #if self.card_sum == 21:
            #return result function
        print(self.card_sum)

        if self.card_sum <= 21:
            self.display.text = str(self.card_sum)
        elif self.card_sum > 21:
            return self.a_value_check()

    def a_value_check(self):
        ###checking A amount
        number_of_a = 0
        for i in self.card_sum_list:
            if i == 11:
                number_of_a += 1

        if number_of_a > 0:
            self.card_sum -= 10
            self.display.text = str(self.card_sum)
            if self.card_sum > 21:
                if number_of_a > 1:
                    self.card_sum -= 10
                    self.display.text = str(self.card_sum)
                    if self.card_sum > 21:
                        if number_of_a > 2:
                            self.card_sum -= 10
                            self.display.text = str(self.card_sum)
                            if number_of_a > 3:
                                self.card_sum -= 10
                                self.display.text = str(self.card_sum)
                            else:
                                self.display.text = "Boom!" + str(self.card_sum) + ", Try again!"
                        else:
                            self.display.text = "Boom!" + str(self.card_sum) + ", Try again!"
                else:
                    self.display.text = "Boom!" + str(self.card_sum) + ", Try again!"
        else:
            self.display.text = "Boom!" + str(self.card_sum) + ", Try again!"

        if self.display.text == "Boom!" + str(self.card_sum) + ", Try again!":
            self.call_card.disabled = True

    def deal(self, instance):
        ##Host card 1
        if self.house_card1.text == "":
            self.hc1 += 0
        elif self.house_card1.text != "":
            if self.house_card1.text in ("11", "12", "13"):
                self.hc1 += 10
            elif self.house_card1.text == "1":
                self.hc1 += 11
            else:
                self.hc1 += int(self.house_card1.text)
        ## Host card 2
        if self.house_card2.text == "":
            self.hc2 += 0
        elif self.house_card2.text != "":
            if self.house_card2.text in ("11", "12", "13"):
                self.hc2 += 10
            elif self.house_card2.text == "1":
                self.hc2 += 11
            else:
                self.hc2 += int(self.house_card2.text)
        ## Host card 3
        h_c_3 = sample(self.card_list_total, 1)
        for i in h_c_3:
            self.card_list_total.remove(i)
            self.house_card3.text = str(i)
        if self.house_card3.text == "":
            self.hc3 += 0
        elif self.house_card3.text != "":
            if self.house_card3.text in ("11", "12", "13"):
                self.hc3 += 10
            elif self.house_card3.text == "1":
                self.hc3 += 11
            else:
                self.hc3 += int(self.house_card3.text)
        h_c_4 = sample(self.card_list_total, 1)
        for i in h_c_4:
            self.card_list_total.remove(i)
            self.house_card4.text = str(i)
        if self.house_card4.text == "":
            self.hc4 += 0
        elif self.house_card4.text != "":
            if self.house_card4.text in ("11", "12", "13"):
                self.hc4 += 10
            elif self.house_card4.text == "1":
                self.hc4 += 11
            else:
                self.hc4 += int(self.house_card4.text)
        h_c_5 = sample(self.card_list_total, 1)
        for i in h_c_5:
            self.card_list_total.remove(i)
            self.house_card5.text = str(i)
        if self.house_card5.text == "":
            self.hc5 += 0
        elif self.house_card5.text != "":
            if self.house_card5.text in ("11", "12", "13"):
                self.hc5 += 10
            elif self.house_card5.text == "1":
                self.hc5 += 11
            else:
                self.hc5 += int(self.house_card5.text)
        h_c_6 = sample(self.card_list_total, 1)
        for i in h_c_6:
            self.card_list_total.remove(i)
            self.house_card6.text = str(i)
        if self.house_card6.text == "":
            self.hc6 += 0
        elif self.house_card6.text != "":
            if self.house_card6.text in ("11", "12", "13"):
                self.hc6 += 10
            elif self.house_card6.text == "1":
                self.hc6 += 11
            else:
                self.hc6 += int(self.house_card6.text)
        self.house_sum_list = [self.hc1, self.hc2, self.hc3, self.hc4, self.hc5, self.hc6]
        self.house_sum = self.hc1 + self.hc2
        print(self.house_sum)
        ## Checking a in host hand
        a_in_house = 0
        for h in self.house_sum_list:
            if h == 11:
                a_in_house += 1

        if self.house_sum > 21:
            if "1" in (self.house_card1.text, self.house_card2.text):
                self.house_sum -= 10
                if self.house_sum < 17:
                    self.add_widget(self.house_card3)
                    self.house_sum += self.hc3
                    if self.house_sum > 21:
                        if self.house_card3.text == "1":
                            self.house_sum -= 10
                            if self.house_sum < 17:
                                self.add_widget(self.house_card4)
                                self.house_sum += self.hc4
                                if self.house_sum > 21:
                                    if self.house_card4.text == "1":
                                        self.house_sum -= 10
                                        if self.house_sum < 17:
                                            self.add_widget(self.house_card5)
                                            self.house_sum += self.hc5
                                            if self.house_sum < 17:
                                                self.add_widget(self.house_card6)
                                                self.house_sum += self.hc6
                                                if self.house_sum > 21:
                                                    self.display.text = "You Win"
                                        elif self.house_sum > 21:
                                            self.display.text = "You Win"
                                    else:
                                        self.display.text = "You Win"
                                elif self.house_sum < 17:
                                    self.add_widget(self.house_card5)
                                    self.house_sum += self.hc5
                                    if self.house_sum > 21:
                                        self.display.text = "You Win"
                                    elif self.house_sum < 17:
                                        self.add_widget(self.house_card6)
                                        self.house_sum += self.hc6
                                        if self.house_sum > 21:
                                            self.display.text = "You Win"
                        else:
                            self.display.text = "You Win"
                    elif self.house_sum < 17:
                        self.add_widget(self.house_card4)
                        self.house_sum += self.hc4
                        if self.house_sum > 21:
                            if self.house_card4.text == "1":
                                self.house_sum -= 10
                                if self.house_sum < 17:
                                    self.add_widget(self.house_card5)
                                    self.house_sum += self.hc5
                                    if self.house_sum > 21:
                                        if self.house_card5.text == "1":
                                            self.house_sum -= 10
                                            if self.house_sum < 17:
                                                self.add_widget(self.house_card6)
                                                self.house_sum += self.hc6
                                                if self.house_sum > 21:
                                                    if self.house_card6.text == "1":
                                                        self.house_sum -= 10
                                                    else:
                                                        self.display.text = "You Win"
                                        else:
                                            self.display.text = "You Win"
                                    elif self.house_sum < 17:
                                        self.add_widget(self.house_card6)
                                        self.house_sum += self.hc6
                                        if self.house_sum > 21:
                                            if self.house_card6.text == "1":
                                                self.house_sum -= 10
                                            else:
                                                self.display.text = "You Win"
                            else:
                                self.display.text = "You Win"
                        elif self.house_sum < 17:
                            self.add_widget(self.house_card5)
                            self.house_sum += self.hc5
                            if self.house_sum > 21:
                                if self.house_card5.text == "1":
                                    self.house_sum -= 10
                                    if self.house_sum < 17:
                                        self.add_widget(self.house_card6)
                                        self.house_sum += self.hc6
                                        if self.house_sum > 21:
                                            if self.house_card6.text == "1":
                                                self.house_sum -= 10
                                            else:
                                                self.display.text = "You Win"
                                else:
                                    self.display.text = "You Win"
                            elif self.house_sum < 17:
                                self.add_widget(self.house_card6)
                                self.house_sum += self.hc6
                                if self.house_sum > 21:
                                    if self.house_card6.text == "1":
                                        self.house_sum -= 10
                                    else:
                                        self.display.text = "You Win"
            else:
                self.display.text = "You Win"

        elif self.house_sum < 17:
            self.add_widget(self.house_card3)
            self.house_sum += self.hc3
            if self.house_sum > 21:
                if "1" in (self.house_card1.text, self.house_card2.text, self.house_card3.text):
                    self.house_sum -= 10
                    if self.house_sum < 17:
                        self.add_widget(self.house_card4)
                        self.house_sum += self.hc4
                        if self.house_sum > 21:
                            if "1" in (self.house_card1.text, self.house_card2.text) and self.house_card3.text == "1":
                                self.house_sum -= 10
                                if self.house_sum < 17:
                                    self.add_widget(self.house_card4)
                                    self.house_sum += self.hc4
                                    if self.house_sum > 21:
                                        if self.house_card4.text == "1":
                                            self.house_sum -= 10
                                            if self.house_sum < 17:
                                                self.add_widget(self.house_card5)
                                                self.house_sum += self.hc5
                                                if self.house_sum > 21:
                                                    if self.house_card5.text == "1":
                                                        self.house_sum -= 10
                                                        if self.house_sum < 17:
                                                            self.add_widget(self.house_card6)
                                                            self.house_sum += self.hc6
                                                            if self.house_sum > 21:
                                                                self.display.text = "You Win"
                                                    else:
                                                        self.display.text = "You Win"
                                                elif self.house_sum < 17:
                                                    self.add_widget(self.house_card6)
                                                    self.house_sum += self.hc6
                                                    if self.house_sum > 21:
                                                        self.display.text = "You Win"
                                        else:
                                            self.display.text = "You Win"
                                    elif self.house_sum < 17:
                                        self.add_widget(self.house_card5)
                                        self.house_sum += self.hc5
                                        if self.house_sum > 21:
                                            if self.house_card5.text == "1":
                                                self.house_sum -= 10
                                                if self.house_sum < 17:
                                                    self.add_widget(self.house_card6)
                                                    self.house_sum += self.hc6
                                                    if self.house_sum > 21:
                                                        self.display.text = "You Win"
                                            else:
                                                self.display.text = "You Win"
                                        elif self.house_sum < 17:
                                            self.add_widget(self.house_card6)
                                            self.house_sum += self.hc6
                                            if self.house_sum > 21:
                                                self.display.text = "You Win"

                            else:
                                self.display.text = "You Win"

                        elif self.house_sum < 17:
                            self.add_widget(self.house_card5)
                            self.house_sum += self.hc5
                            if self.house_sum > 21:
                                if self.house_card5.text == "1":
                                    self.house_sum -= 10
                                    if self.house_sum < 17:
                                        self.add_widget(self.house_card6)
                                        self.house_sum += self.hc6
                                        if self.house_sum > 21:
                                            self.display.text = "You Win"
                            elif self.house_sum < 17:
                                self.add_widget(self.house_card6)
                                self.house_sum += self.hc6
                                if self.house_sum > 21:
                                    self.display.text = "You Win"
                else:
                    self.display.text = "You Win"
###
            elif self.house_sum < 17:
                self.add_widget(self.house_card4)
                self.house_sum += self.hc4
                if self.house_sum > 21:
                    if self.house_card4.text == "1":
                        self.house_sum -= 10
                        if self.house_sum < 17:
                            self.add_widget(self.house_card5)
                            self.house_sum += self.hc5
                            if self.house_sum > 21:
                                if self.house_card5.text == "1":
                                    self.house_sum -= 10
                                    if self.house_sum < 17:
                                        self.add_widget(self.house_card6)
                                        self.house_sum += self.hc6
                                        if self.house_sum > 21:
                                            self.display.text = "You Win"

                                        elif self.house_sum < 17:
                                            self.add_widget(self.house_card6)
                                            self.house_sum += self.hc6
                                            if self.house_sum > 21:
                                                self.display.text = "You Win"
                                else:
                                    self.display.text = "You Win"
                            #
                            elif self.house_sum < 17:
                                self.add_widget(self.house_card6)
                                self.house_sum += self.hc6
                                self.display.text = "You Win"

                    else:
                        self.display.text = "You Win"

                elif self.house_sum < 17:
                    self.add_widget(self.house_card5)
                    self.house_sum += self.hc5
                    if self.house_sum > 21:
                        if self.house_card5.text == "1":
                            self.house_sum -= 10
                            if self.house_sum < 17:
                                self.add_widget(self.house_card6)
                                self.house_sum += self.hc6
                                if self.house_sum > 21:
                                    self.display.text = "You Win"
                    elif self.house_sum < 17:
                        self.add_widget(self.house_card6)
                        self.house_sum += self.hc6
                        if self.house_sum > 21:
                            self.display.text = "You Win"

        if self.display.text != "You Win":
            if self.house_sum > self.card_sum:
                self.display.text = "You lose"
            elif self.house_sum < self.card_sum:
                self.display.text = "You Win"
            elif self.house_sum == self.card_sum:
                self.display.text = "Draw game"
        self.remove_widget(self.house_card2_cover)
        self.call_card.disabled = True
        print(self.hc1)
        print(self.hc2)
        print(self.hc3)
        print(self.hc4)
        print(self.hc5)
        print(self.hc6)

        print(self.house_sum)
        print(self.card_sum)


class BlackJackApp(App):
    def build(self):
        return BlackJackTable()


if __name__ == "__main__":
    BlackJackApp().run()