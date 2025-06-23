# Agentic Coding Rules and Templates

A collection of agentic coding rules and templates for use with tools like Cline and Roo Code.

## Setup

```shell
git clone git@gitlab.mantelgroup.com.au:genai/agentic-coding-rules-and-templates.git
cd agentic-coding-rules-and-templates
git submodule update --init --recursive
```

## Using Cline Rules

Copy rules from `cline/.clinerules/` to `.clinerules/` in your project root. Cline automatically discovers and uses rules from this folder.

### Quick Setup
```shell
# Create rules directory in your project
mkdir .clinerules

# Copy relevant rules (examples)
cp cline/.clinerules/generic/* /path/to/your/project/.clinerules/
cp cline/.clinerules/frameworks/cdk.xml /path/to/your/project/.clinerules/  # if using AWS CDK
```

### Available Rules

**Generic Rules** (`cline/.clinerules/generic/`):
- `agent-rules.xml` - Core agent behavior, reasoning, and response patterns
- `dev-standards.xml` - Development standards, coding practices, testing guidelines
- `analysis.xml` - Systematic analysis framework with confidence assessment

**Framework Rules** (`cline/.clinerules/frameworks/`):
- `cdk.xml` - AWS CDK development guidelines and best practices

**Prompts** (`cline/.clinerules/prompts/`):
- `prompts_claude4.md` - Claude 4 specific prompt engineering techniques. Use it to create new prompts

### Usage Tips

- Start with generic rules (`agent-rules.xml` + `dev-standards.xml`)
- Add framework-specific rules as needed
- Customize rules for your project's naming conventions and standards
- Include `.clinerules/` in version control for team consistency

## Sample Prompts

**Repository Analysis** (`cline/sample_prompts/repository-analysis.txt`):
- Comprehensive analysis prompt for understanding existing repository architecture, user flows, and data flows

### Using Sample Prompts
Copy and paste the content from sample prompt files directly into your Cline conversation to execute complex analysis tasks with structured outputs.

## Individual Mantelorian's Rules

See [individuals](individuals) which contains directories or git submodules for rules and templates that people have shared.
