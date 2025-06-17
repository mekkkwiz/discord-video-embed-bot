#!/usr/bin/env python3
"""
Test script for team generator utility functions.
This script can be used to test the team generation logic without running the full Discord bot.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.team_generator import generate_teams, validate_team_input


def test_basic_team_generation():
    """Test basic team generation functionality."""
    people = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry"]
    num_teams = 3

    result = generate_teams(people, num_teams)

    assert result['num_teams'] == num_teams
    assert result['total_people'] == len(people)
    assert set(sum(result['teams'].values(), [])) == set(people)
    assert result['min_team_size'] <= result['max_team_size']
    assert abs(result['average_team_size'] - (len(people) / num_teams)) < 1e-6


def test_input_validation():
    """Test input validation functionality."""
    test_cases = [
        ("Alice,Bob,Charlie,Diana", 4, True),
        ("Alice, Bob , Charlie,Diana ", 4, True),
        ("Alice,Bob,Alice,Charlie", 3, True),
        ("", 0, False),
        ("Alice", 1, True),
        ("Alice,Bob,Charlie,Diana,Eve,Frank,Grace,Henry,Ivy,Jack", 10, True)
    ]

    for input_str, expected_count, should_pass in test_cases:
        if should_pass:
            people = validate_team_input(input_str)
            assert len(people) == expected_count
        else:
            import pytest
            with pytest.raises(ValueError):
                validate_team_input(input_str)


def test_edge_cases():
    """Test edge cases and error conditions."""
    import pytest

    # Test with more teams than people
    people = ["Alice", "Bob"]
    with pytest.raises(ValueError):
        generate_teams(people, 3)

    # Test with exact number of teams as people
    people = ["Alice", "Bob", "Charlie"]
    result = generate_teams(people, 3)
    assert all(len(members) == 1 for members in result['teams'].values())

    # Test with large number of people
    people = [f"Person{i}" for i in range(1, 101)]  # 100 people
    result = generate_teams(people, 10)
    sizes = [len(team) for team in result['teams'].values()]
    assert min(sizes) >= 10
    assert max(sizes) <= 10
    assert sum(sizes) == 100


def interactive_test():
    """Interactive test for manual testing."""
    print("\n=== Interactive Test ===")
    print("Enter people names (comma-separated) or 'quit' to exit:")
    
    while True:
        try:
            people_input = input("> ").strip()
            if people_input.lower() == 'quit':
                break
            
            if not people_input:
                continue
            
            people = validate_team_input(people_input)
            
            num_teams = int(input(f"Number of teams for {len(people)} people: "))
            
            result = generate_teams(people, num_teams)
            
            print(f"\n🎲 Generated Teams:")
            for team_name, members in result['teams'].items():
                print(f"  {team_name}: {', '.join(members)}")
            print()
            
        except ValueError as e:
            print(f"❌ Error: {e}")
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
    
    print("Goodbye!")


if __name__ == "__main__":
    print("Discord Bot Team Generator - Test Suite")
    print("=" * 50)
    
    test_basic_team_generation()
    test_input_validation()
    test_edge_cases()
    
    # Uncomment the next line for interactive testing
    # interactive_test()
    
    print("\n🎯 All tests completed!")
    print("\nTo test the Discord bot:")
    print("1. Make sure your bot is running")
    print("2. Use the slash command: /teams <num_teams> <num_people> <people_list>")
    print("3. Example: /teams 2 6 Alice,Bob,Charlie,Diana,Eve,Frank")
    print("4. Use /teamhelp for more information")
