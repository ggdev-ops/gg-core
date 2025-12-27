# ggdev - Android Development Tools

`ggdev` is a command-line tool for simplifying Android development on Termux. Its primary goal is to solve complex installation and environment issues with single, memorable commands.

The tool is managed within the [gg-core](https://github.com/ggdev-ops/gg-core) monorepo.

## The Legendary Solution

The `ggdev` tool was born out of the need to create a repeatable, one-command solution for installing `@google/gemini-cli` on Android/Termux, a process that was previously plagued with `node-gyp` and native dependency errors.

The core solution is the command:
```bash
ggdev in gemini devs-night
```
This command correctly configures the environment to solve at least 7 known GitHub issues related to the problem.

## Command Suite

### Complete Command Structure
```bash
ggdev <command> [arguments]

# INFO COMMANDS (Show what's available)
gradle               Show Gradle versions and info
sdk                  Show Android SDK info
agent                Show available CLI agents

# INSTALL COMMANDS
in gradle [version]  Install Gradle (default: 8.14.3)
in sdk               Install Android SDK
in <agent> [tag]     Install CLI agent (e.g., gemini)

# REMOVE COMMANDS
remove gradle        Remove Gradle installation
remove sdk           Remove Android SDK
remove <agent>       Remove CLI agent

# OTHER COMMANDS
verify               Verify all installations
update               Update existing tools
```

### Usage Examples
```bash
ggdev gradle                     # Show Gradle info
ggdev in gradle 8.14.3           # Install Gradle 8.14.3
ggdev in sdk                     # Install Android SDK
ggdev agent                      # Show available agents
ggdev in gemini                  # Install gemini-cli (stable)
ggdev in gemini devs-night       # Install nightly version
ggdev remove gradle              # Remove Gradle
ggdev verify                     # Check everything
```