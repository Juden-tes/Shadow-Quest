class Quest:
    def __init__(self, description: str,
                 reward_coins: int,
                 reward_xp: int,
                 required_kills: int) -> None:
        self.description     = description
        self.reward_coins    = reward_coins
        self.reward_xp       = reward_xp
        self.required_kills  = required_kills
        self.completed       = False

    def check_completion(self, player) -> None:
        """
        Call after every fight.  If the player has enough kills and the quest
        isn’t completed yet, pay out the rewards.
        """
        if self.completed:
            return

        if player.enemies_defeated >= self.required_kills:
            self.completed = True
            player.add_coins(self.reward_coins)
            player.exp += self.reward_xp
            print(f"📜  Quest completed: {self.description} "
                  f"(+{self.reward_coins} coins, +{self.reward_xp} XP)")


class QuestSystem:
    """
    Holds a list of quests and offers two convenience helpers:
      • show_quests()     – print a tidy list for the player
      • update_quests()   – run after combat to unlock finished quests
    """
    def __init__(self, quests=None) -> None:
        self.quests = quests if quests else []

    def show_quests(self) -> None:
        print("\n📜  **Quests**")
        for q in self.quests:
            status = "✓" if q.completed else "…"
            print(f" {status}  {q.description}"
                  f"  ({q.required_kills} kills, "
                  f"{q.reward_coins} c / {q.reward_xp} XP)")

    def update_quests(self, player) -> None:
        for q in self.quests:
            q.check_completion(player)