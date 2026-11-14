"""Game-specific configuration file, inherits from src/config/config.py"""

import os
from src.config.config import Config
from src.config.distributions import Distribution
from src.config.betmode import BetMode


class GameConfig(Config):

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        self.game_id ="neon_outlaw"
      
        self.provider_number = 0
        self.working_name = "Sample Lines Game"
        self.wincap = 100000.0
        self.win_type = "lines"
        self.rtp = 0.9650
        self.construct_paths()

        # Game Dimensions
        self.num_reels = 5
        self.num_rows = [3] * self.num_reels
        # Board and Symbol Properties
        self.paytable = {
            (5, "W"): 50,
            (4, "W"): 20,
            (3, "W"): 10,
            (5, "H1"): 50,
            (4, "H1"): 20,
            (3, "H1"): 10,
            (5, "H2"): 15,
            (4, "H2"): 5,
            (3, "H2"): 3,
            (5, "H3"): 10,
            (4, "H3"): 3,
            (3, "H3"): 2,
            (5, "H4"): 8,
            (4, "H4"): 2,
            (3, "H4"): 1,
            (5, "H5"): 6,
            (4, "H5"): 1.5,
            (3, "H5"): 0.8,
            (5, "L1"): 5,
            (4, "L1"): 1,
            (3, "L1"): 0.5,
            (5, "L2"): 3,
            (4, "L2"): 0.7,
            (3, "L2"): 0.3,
            (5, "L3"): 3,
            (4, "L3"): 0.7,
            (3, "L3"): 0.3,
            (5, "L4"): 2,
            (4, "L4"): 0.5,
            (3, "L4"): 0.2,
            (5, "L5"): 1,
            (4, "L5"): 0.3,
            (3, "L5"): 0.1,
        }

        self.paylines = {
            1: [
                0,
                0,
                0,
                0,
                0,
            ],
            2: [
                1,
                1,
                1,
                1,
                1,
            ],
            3: [
                2,
                2,
                2,
                2,
                2,
            ],
            4: [
                0,
                1,
                2,
                1,
                0,
            ],
            5: [
                2,
                1,
                0,
                1,
                2,
            ],
            6: [
                0,
                0,
                1,
                2,
                2,
            ],
            7: [
                2,
                2,
                1,
                0,
                0,
            ],
            8: [
                1,
                0,
                1,
                2,
                1,
            ],
            9: [
                1,
                2,
                1,
                0,
                1,
            ],
            10: [
                0,
                1,
                1,
                1,
                2,
            ],
            11: [
                2,
                1,
                1,
                1,
                0,
            ],
            12: [
                0,
                1,
                0,
                1,
                2,
            ],
            13: [
                2,
                1,
                2,
                1,
                0,
            ],
            14: [
                1,
                1,
                0,
                1,
                1,
            ],
            15: [
                1,
                1,
                2,
                1,
                1,
            ],
            16: [
                0,
                2,
                1,
                0,
                2,
            ],
            17: [
                2,
                0,
                1,
                2,
                0,
            ],
            18: [
                0,
                0,
                2,
                0,
                0,
            ],
            19: [
                2,
                2,
                0,
                2,
                2,
            ],
            20: [
                1,
                0,
                0,
                0,
                1,
            ],
        }

        self.include_padding = True
        self.special_symbols = {"wild": ["W"], "scatter": ["S"], "multiplier": ["W"]}

        self.freespin_triggers = {
            self.basegame_type: {3: 12, 4: 15, 5: 20},
            self.freegame_type: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
        }
        self.anticipation_triggers = {
            self.basegame_type: min(self.freespin_triggers[self.basegame_type].keys()) - 1,
            self.freegame_type: min(self.freespin_triggers[self.freegame_type].keys()) - 1,
        }
        # Reels
        reels = {"BR0": "BR0.csv", "FR0": "FR0.csv", "WCAP": "FRWCAP.csv"}
        self.reels = {}
        for r, f in reels.items():
            self.reels[r] = self.read_reels_csv(os.path.join(self.reels_path, f))

        self.padding_reels[self.basegame_type] = self.reels["BR0"]
        self.padding_reels[self.freegame_type] = self.reels["FR0"]
        self.padding_symbol_values = {"W": {"multiplier": {2: 100, 3: 50, 4: 50, 5: 50, 10: 30, 20: 20, 50: 5}}}

        freegame_condition = {
            "reel_weights": {
                self.basegame_type: {"BR0": 1},
                self.freegame_type: {"FR0": 1},
            },
            "scatter_triggers": {3: 50, 4: 20, 5: 5},
            "mult_values": {
                self.basegame_type: {1: 1},
                self.freegame_type: {
                    2: 600,
                    3: 800,
                    4: 500,
                    5: 200,
                    10: 150,
                    20: 100,
                    50: 50,
                    100: 3,
                    200: 2,
                    500: 1,
                    1000: 1,
                },
            },
            "force_wincap": False,
            "force_freegame": True,
        }

        basegame_condition = {
            "reel_weights": {self.basegame_type: {"BR0": 1}},
            "mult_values": {self.basegame_type: {1: 1}},
            "force_wincap": False,
            "force_freegame": False,
        }

        wincap_condition = {
            "reel_weights": {
                self.basegame_type: {"BR0": 1},
                self.freegame_type: {"FR0": 1, "WCAP": 5},
            },
            "mult_values": {
                self.basegame_type: {1: 1},
                self.freegame_type: {2: 10, 3: 20, 4: 50, 5: 60, 10: 100, 20: 90, 50: 50, 100:40, 200:30, 500:20, 1000:10},
            },
            "scatter_triggers": {4: 1, 5: 2},
            "force_wincap": True,
            "force_freegame": True,
        }

        zerowin_condition = {
            "reel_weights": {self.basegame_type: {"BR0": 1}},
            "mult_values": {
                self.basegame_type: {1: 1},
                self.freegame_type: {2: 100, 3: 80, 4: 50, 5: 20, 10: 10, 20: 5, 50: 1},
            },
            "force_wincap": False,
            "force_freegame": False,
        }

        mode_maxwins = {"base": 100000, "bonus": 100000, "ante": 100000}
        # Contains all game-logic simulation conditions
        self.bet_modes = [
            BetMode(
                name="base",
                cost=1.0,
                rtp=self.rtp,
                max_win=mode_maxwins["base"],
                auto_close_disabled=False,
                is_feature=True,
                is_buybonus=False,
                distributions=[
                    Distribution(
                        criteria="wincap",
                        quota=0.001,
                        win_criteria=mode_maxwins["base"],
                        conditions=wincap_condition,
                    ),
                    Distribution(criteria="freegame", quota=0.1, conditions=freegame_condition),
                    Distribution(criteria="0", quota=0.4, win_criteria=0.0, conditions=zerowin_condition),
                    Distribution(criteria="basegame", quota=0.5, conditions=basegame_condition),
                ],
            ),
            BetMode(
                name="bonus",
                cost=100.0,
                rtp=self.rtp,
                max_win=mode_maxwins["bonus"],
                auto_close_disabled=False,
                is_feature=False,
                is_buybonus=True,
                distributions=[
                    Distribution(
                        criteria="wincap",
                        quota=0.001,
                        win_criteria=mode_maxwins["bonus"],
                        conditions=wincap_condition,
                    ),
                    Distribution(criteria="freegame", quota=0.1, conditions=freegame_condition),
                ],

               
            ),
            # Enhanced Spins (ante): the base game at 2x cost with Vault Spins triggering ~4x as often.
            # Same reels, scatter weights, multipliers and force flags as base; only quotas and
            # optimisation targets (game_optimization.py) differ.
            BetMode(
                name="ante",
                cost=3.0,
                rtp=self.rtp,
                max_win=mode_maxwins["ante"],
                auto_close_disabled=False,
                is_feature=True,
                is_buybonus=False,
                distributions=[
                    Distribution(
                        criteria="wincap",
                        quota=0.001,
                        win_criteria=mode_maxwins["ante"],
                        conditions=wincap_condition,
                    ),
                    Distribution(criteria="freegame", quota=0.2, conditions=freegame_condition),
                    Distribution(criteria="0", quota=0.3, win_criteria=0.0, conditions=zerowin_condition),
                    Distribution(criteria="basegame", quota=0.5, conditions=basegame_condition),
                ],
            ),
            BetMode(
            name="max_or_nothing",
            cost=1000.0,
            rtp=self.rtp,
            max_win=mode_maxwins["bonus"],
            auto_close_disabled=False,
            is_feature=False,
            is_buybonus=True,
            distributions=[
                Distribution(criteria="wincap", quota=0.00965, win_criteria=mode_maxwins["bonus"], conditions=wincap_condition),
                Distribution(criteria="0", quota=0.99035, win_criteria=0.0, conditions=zerowin_condition),
            ],
            ),
            




        ]
