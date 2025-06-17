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
    print("=== Testing Basic Team Generation ===")
    
    people = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry"]
    num_teams = 3
    
    try:
        result = generate_teams(people, num_teams)
        
        print(f"Generated {result['num_teams']} teams from {result['total_people']} people:")
        for team_name, members in result['teams'].items():
            print(f"  {team_name}: {', '.join(members)}")
        
        print(f"Team sizes: {result['min_team_size']}-{result['max_team_size']} (avg: {result['average_team_size']:.1f})")
        print("✅ Basic test passed!")
        
    except Exception as e:
        print(f"❌ Basic test failed: {e}")


def test_input_validation():
    """Test input validation functionality."""
    print("\n=== Testing Input Validation ===")
    
    test_cases = [
        ("Alice,Bob,Charlie,Diana", 4, "Valid input"),
        ("Alice, Bob , Charlie,Diana ", 4, "Input with spaces"),
        ("Alice,Bob,Alice,Charlie", 3, "Duplicate names"),
        ("", 0, "Empty input (should fail)"),
        ("Alice", 1, "Single person"),
        ("Alice,Bob,Charlie,Diana,Eve,Frank,Grace,Henry,Ivy,Jack", 10, "10 people")
    ]
    
    for input_str, expected_count, description in test_cases:
        try:
            people = validate_team_input(input_str)
            print(f"✅ {description}: {len(people)} people - {people}")
            if expected_count > 0 and len(people) != expected_count:
                print(f"   ⚠️  Expected {expected_count}, got {len(people)}")
        except ValueError as e:
            print(f"❌ {description}: {e}")


def test_edge_cases():
    """Test edge cases and error conditions."""
    print("\n=== Testing Edge Cases ===")
    
    # Test with more teams than people
    try:
        people = ["Alice", "Bob"]
        result = generate_teams(people, 3)
        print("❌ Should have failed with more teams than people")
    except ValueError as e:
        print(f"✅ Correctly handled more teams than people: {e}")
    
    # Test with exact number of teams as people
    try:
        people = ["Alice", "Bob", "Charlie"]
        result = generate_teams(people, 3)
        print(f"✅ One person per team: {result['teams']}")
    except Exception as e:
        print(f"❌ Failed with one person per team: {e}")
    
    # Test with large number of people
    try:
        people = [f"Person{i}" for i in range(1, 101)]  # 100 people
        result = generate_teams(people, 10)
        sizes = [len(team) for team in result['teams'].values()]
        print(f"✅ Large test (100 people, 10 teams): sizes {min(sizes)}-{max(sizes)}")
    except Exception as e:
        print(f"❌ Failed with large number: {e}")


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
