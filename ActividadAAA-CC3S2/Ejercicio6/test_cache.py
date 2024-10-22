import pytest
from cache import Cache

def test_fifo_policy():
    # Arrange
    cache = Cache(3)
    cache.set_policy("FIFO")

    # Act
    cache.add("A")
    cache.add("B")
    cache.add("C")

    # Assert
    assert cache.items() == ["A", "B", "C"]

    # Act - Add one more item
    cache.add("D")

    # Assert - FIFO should replace "A"
    assert cache.items() == ["B", "C", "D"]

def test_lru_policy():
    # Arrange
    cache = Cache(3)
    cache.set_policy("LRU")

    # Act
    cache.add("A")
    cache.add("B")
    cache.add("C")

    # Assert
    assert cache.items() == ["A", "B", "C"]

    # Act - Access "A", then add "D"
    cache.get("A")
    cache.add("D")

    # Assert - LRU should replace "B"
    assert cache.items() == ["A", "C", "D"]

