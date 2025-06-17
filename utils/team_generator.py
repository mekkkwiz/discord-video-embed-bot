import random
from typing import List, Dict, Any
from utils.logger import setup_logger

logger = setup_logger(__name__)


def generate_teams(people: List[str], num_teams: int) -> Dict[str, Any]:
    """
    Generate random teams from a list of people.
    
    Args:
        people: List of person names
        num_teams: Number of teams to create
        
    Returns:
        Dictionary containing teams and metadata
        
    Raises:
        ValueError: If invalid parameters are provided
    """
    if not people:
        raise ValueError("People list cannot be empty")
    
    if num_teams <= 0:
        raise ValueError("Number of teams must be positive")
    
    if len(people) < num_teams:
        raise ValueError(f"Cannot create {num_teams} teams with only {len(people)} people")
    
    # Remove duplicates and strip whitespace.
    # Note: Using a set here loses the original order of names, but since we shuffle later, this is acceptable.
    unique_people = list(set(name.strip() for name in people if name.strip()))
    
    if len(unique_people) < num_teams:
        raise ValueError(f"After removing duplicates, cannot create {num_teams} teams with only {len(unique_people)} unique people")
    
    logger.info(f"Generating {num_teams} teams from {len(unique_people)} people")
    
    # Shuffle the people list for randomization
    shuffled_people = unique_people.copy()
    random.shuffle(shuffled_people)
    
    # Initialize teams
    teams = {f"Team {i+1}": [] for i in range(num_teams)}
    team_names = list(teams.keys())
    
    # Distribute people evenly across teams
    for i, person in enumerate(shuffled_people):
        team_index = i % num_teams
        teams[team_names[team_index]].append(person)
    
    # Calculate team statistics
    team_sizes = [len(team) for team in teams.values()]
    
    result = {
        "teams": teams,
        "total_people": len(unique_people),
        "num_teams": num_teams,
        "min_team_size": min(team_sizes),
        "max_team_size": max(team_sizes),
        "average_team_size": sum(team_sizes) / len(team_sizes)
    }
    
    logger.info(f"Teams generated successfully: {result['num_teams']} teams, "
                f"sizes range from {result['min_team_size']} to {result['max_team_size']}")
    
    return result


def validate_team_input(people_str: str) -> List[str]:
    """
    Validate and parse the people input string.
    
    Args:
        people_str: Comma-separated string of people names
        
    Returns:
        List of validated person names (duplicates preserved for user feedback)
        
    Raises:
        ValueError: If input is invalid
    """
    if not people_str or not people_str.strip():
        raise ValueError("People list cannot be empty")
    
    # Split by comma and clean up names
    people = [name.strip() for name in people_str.split(',') if name.strip()]
    
    if not people:
        raise ValueError("No valid names found in the input")
    
    # Check for reasonable name lengths
    for name in people:
        if len(name) > 100:  # Discord username limit consideration
            raise ValueError(f"Name '{name[:50]}...' is too long (max 100 characters)")
        if len(name) < 1:
            raise ValueError("Empty names are not allowed")
    
    logger.debug(f"Validated {len(people)} people from input")
    return people
