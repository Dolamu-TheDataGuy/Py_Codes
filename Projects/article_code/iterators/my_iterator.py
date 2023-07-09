from typing import Iterable
from dataclasses import dataclass


@dataclass
class InfiniteNumberIterator:
    num: int = 0


    def __iter__(self):
        return self
    
    def __next__(self) -> int:
        self.num += 1
        return self.num
    

@dataclass
class NumberIterator:
    max: int
    num: int = 0


    def __iter__(self):
        return self
    
    def __next__(self) -> int:
        if self.num >= self.max:
            raise StopIteration
        self.num += 1
        return self.num
    

def main() -> None:
    print(NumberIterator(3))
    for num in NumberIterator(3,1):
        print(num)

if __name__ == "__main__":
    main()




