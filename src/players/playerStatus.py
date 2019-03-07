import Player
import math


players_map = {}


# function to add players to matchPlayers
# must take the current active players as argument that are available on server
# TODO: implement with web sockets on server
# players should be an array of usernames from server
def add_player(players):

    for username in players:
        # TODO: change the x and y coordinates of each player
        temp_player = Player.Player
        temp_player.username = username
        temp_player.x = 0
        temp_player.y = 0
        temp_player.health = 100
        temp_player.kills = 0

        players_map[username] = temp_player

    return players_map


# TODO: finish this
def top_ten():
    top_ten_username = []

    for player in players_map:

        if not top_ten_username:
            top_ten.append(player.key)


# checks if the player object's health reaches zero
def is_dead(player):
    if player.health <= 0:
        return True
    else:
        return False


# checks if prey is withing range of predator weapon
def within_range(predator, prey):
    distance = math.sqrt(pow((predator.x - prey.x), 2) + pow((predator.y - prey.y), 2))
    if distance <= predator.attack_range:
        return True
    else:
        return False


# prey hit, reduces health based on predator attack
# checks if prey is dead and gets rid of them from player list
def hit_player(prey, predator):
    predator_attack = players_map[predator].weapon.damage
    players_map[prey].health -= predator_attack
    if is_dead(prey):
        players_map.pop(prey)


# changes weapon held
# TODO: finish this when figure out range
def pick_up_weapon(weapon, player):
    new_damage = weapon.damage
    # new_damage_range = weapon.damage_range
    player.damage = new_damage
    # player.damage_range = new_damage_range


