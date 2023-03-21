from dataclasses import dataclass, field


@dataclass
class Pos:
    x: int
    y: int
    knight: dict = None
    items: list = field(default_factory=list)

    def __repr__(self):
        return '[{}, {}]'.format(self.y, self.x)

    def to_json(self):
        return [self.y, self.x]