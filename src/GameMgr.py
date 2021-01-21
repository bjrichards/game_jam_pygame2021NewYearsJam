# Created by Braeden Richards
# Created on January 5th, 2021
# Desc:


# Includes
import pygame


# Class
class GameMgr():
    def __init__(self, engine):
        self.engine = engine

        self.platforms = []

        self.game_status = None

        self.player_load_pos = None

        self.player_lives = 10
        

    
    def initialize(self):
        self.game_status = 'MENU'

    def load_level(self, level):
        self.engine.gravity = 0
        self.create_active_map()
        self.engine.entityMgr.load_map()
        self.engine.gfxMgr.scroll[0] = self.engine.entityMgr.furthest_object 

        self.game_status = 'ENTRY_ANIMATION'
        self.engine.gravity = self.engine.config.gravity


    def tick(self, dt):
        if self.game_status == 'START':
            self.load_level(1)


    def shutdown(self):
        pass

    def create_active_map(self):
        self.platforms = []
        self.enemies = []

        scale = (32, 32)

        nmap = []
        
        row = 0
        col = 0

        pwidth = 0
        pstart = 0
        pactive = False

        c_height = 0
        c_start = 0
        c_active = 0

        self.f = open("data\map.txt", 'r')
        for line in self.f.read().split('\n'):
            nmap.append(line)
        self.f.close()

        self.player_load_pos = (0, 0)

        for line in nmap:
            col = 0
            for char in line:                
                # Check for Platform
                if char == 'G':
                    platform = (col * scale[0], row * scale[1], 'G')
                    self.platforms.append(platform)
                elif char == 'D':
                    platform = (col * scale[0], row * scale[1], 'D')
                    self.platforms.append(platform)
                elif char == 'I':
                    platform = (col * scale[0], row * scale[1], 'I')
                    self.platforms.append(platform)

                elif char == 'X':
                    self.player_load_pos = (col * scale[0], row * scale[1])

                elif char == '0':
                    enemy = (col * scale[0], row * scale[1])
                    self.enemies.append(enemy)

                col += 1
            row += 1