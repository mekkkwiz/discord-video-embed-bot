# Team Generator Feature

## Overview
The Team Generator feature allows you to randomly divide a list of people into teams using Discord slash commands.

## Commands

### `/teams` - Generate Random Teams
**Usage:** `/teams <num_teams> <num_people> <people_list>`

**Parameters:**
- `num_teams`: Number of teams to create (1-20)
- `num_people`: Total number of people (for validation)
- `people_list`: Comma-separated list of people names

**Example:**
```
/teams 2 6 Alice,Bob,Charlie,Diana,Eve,Frank
```

This will create 2 teams from the 6 people listed.

### `/teamhelp` - Show Help
Displays detailed help information about team generation commands.

## Features

### Smart Input Handling
- Automatically removes extra spaces from names
- Handles duplicate names by removing them
- Validates name lengths (max 100 characters)
- Provides clear error messages for invalid input

### Even Distribution
- Teams are distributed as evenly as possible
- If people don't divide evenly, some teams may have one extra person
- Shows team size information in the results

### Rich Discord Integration
- Beautiful embed responses with color coding
- User avatar and timestamp in results
- Organized team display with member counts
- Error handling with user-friendly messages

### Logging and Monitoring
- Comprehensive logging for all team generation activities
- Error tracking for debugging
- User activity monitoring for administration

## Technical Implementation

### Files Structure
```
cogs/
├── team_manager.py     # Discord cog with slash commands
utils/
├── team_generator.py   # Core team generation logic
test_teams.py          # Test suite for validation
```

### Core Functions

#### `generate_teams(people, num_teams)`
- Main function for team generation
- Returns detailed results with team assignments and statistics
- Handles edge cases and validation

#### `validate_team_input(people_str)`
- Parses comma-separated people list
- Validates input format and constraints
- Returns cleaned list of names

### Error Handling
- Validates all input parameters
- Provides specific error messages
- Graceful degradation for edge cases
- Logs all errors for debugging

## Usage Examples

### Basic Team Generation
```
/teams 3 9 Alice,Bob,Charlie,Diana,Eve,Frank,Grace,Henry,Ivy
```
Result: 3 teams with 3 people each

### Uneven Distribution
```
/teams 2 5 Alice,Bob,Charlie,Diana,Eve
```
Result: One team with 3 people, one team with 2 people

### Large Groups
```
/teams 4 20 Person1,Person2,Person3,...,Person20
```
Result: 4 teams with 5 people each

## Testing

Run the test suite to verify functionality:
```bash
python3 test_teams.py
```

The test suite includes:
- Basic team generation tests
- Input validation tests
- Edge case handling
- Large group testing
- Interactive testing mode

## Logging

All team generation activities are logged with:
- User information (who requested teams)
- Team parameters (number of teams, people count)
- Success/failure status
- Error details when applicable
- Performance metrics

Log files are stored in `logs/discord-bot.log`.

## Best Practices

### For Users
1. Use clear, readable names
2. Separate names with commas only
3. Avoid very long names
4. Double-check your people count

### For Developers
1. All team logic is in `utils/team_generator.py`
2. Discord-specific code is in `cogs/team_manager.py`
3. Use the logger for all significant events
4. Validate inputs thoroughly
5. Provide helpful error messages

## Limitations

- Maximum 20 teams per generation
- Maximum 100 characters per name
- Discord embed size limitations for very large teams
- No persistence (teams are not saved)

## Future Enhancements

Potential improvements could include:
- Team balancing based on roles/skills
- Saving and recalling team configurations
- Tournament bracket generation
- Team statistics and history
- Integration with Discord roles
