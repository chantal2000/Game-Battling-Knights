class Battle:
    @staticmethod
    def attack(attacker, defendant):
        attack_score = attacker.base_attack + 0.5
        defend_score = defendant.base_defence

        if attacker.equipped:
            attack_score += attacker.equipped.attack

        if defendant.equipped:
            defend_score += defendant.equipped.defence

        return (
            (attacker, defendant)
            if attack_score > defend_score
            else (defendant, attacker)
        )

    @staticmethod
    def kill_knight(knight, status=1):
        loot = knight.equipped
        last_pos = knight.pos

        knight.update_status(status)
        knight.pos = None
        knight.equipped = None
        knight.base_attack = 0
        knight.base_defence = 0

        return loot, last_pos