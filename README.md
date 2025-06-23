# Agentic Coding Rules and Templates

A comprehensive collection of agentic coding rules and templates for use with AI coding assistants like **Cline** and **Roo Code**. This repository provides structured guidelines, best practices, and frameworks to transform AI assistants into systematic, confident development partners that follow enterprise-grade practices.

## 🚀 Quick Start

```shell
git clone git@gitlab.mantelgroup.com.au:genai/agentic-coding-rules-and-templates.git
cd agentic-coding-rules-and-templates
git submodule update --init --recursive
```

## 📁 Repository Structure

```
├── README.md
├── cline/
│   ├── .clinerules/
│   │   ├── generic/           # Core agent behavior rules
│   │   │   ├── agent-rules.xml
│   │   │   ├── dev-standards.xml
│   │   │   ├── analysis.xml
│   │   │   └── memory-bank.md
│   │   ├── frameworks/        # Framework-specific rules
│   │   │   ├── cdk.xml
│   │   │   ├── dotnet.xml
│   │   │   └── terraform.xml
│   │   └── prompts/          # Prompt engineering resources
│   │       └── prompts_claude4.md
│   └── sample_prompts/       # Ready-to-use prompts
│       └── repository-analysis.txt
└── individuals/              # Individual contributor rules
```

## 🎯 What This Repository Provides

### **Core Agent Rules** (`.clinerules/generic/`)

#### **agent-rules.xml** - AI Agent Behavior Framework
- **Role Definition**: Expert software and cloud engineer behavior patterns
- **Memory Management**: Instructions for handling context limitations
- **Task Approach**: Systematic problem breakdown and analysis
- **Response Structure**: Standardized output formatting with confidence levels
- **Diagram Standards**: Mermaid diagram specifications with color themes
- **Context Continuity**: Guidelines for maintaining project understanding across sessions

#### **dev-standards.xml** - Development Standards
- **Code Quality**: Clean, efficient, and simple code solutions
- **Testing Framework**: Comprehensive unit testing guidelines
- **Error Handling**: Defensive coding practices
- **Logging Standards**: Secure and informative logging practices
- **Code Structure**: Modular, functional programming preferences

#### **analysis.xml** - Systematic Analysis Framework
- **Confidence Assessment**: 0-10 scale confidence scoring before implementation
- **Investigation Checklists**: Structured approaches for different system components
- **Risk Mitigation**: Prevents costly mistakes through systematic analysis
- **Documentation Requirements**: Comprehensive analysis documentation templates

#### **memory-bank.md** - Context Persistence System
- **Memory Bank Structure**: Hierarchical documentation system
- **Core Files**: projectbrief.md, productContext.md, activeContext.md, etc.
- **Workflow Integration**: Plan and Act mode workflows
- **Update Triggers**: When and how to maintain documentation

### **Framework-Specific Rules** (`.clinerules/frameworks/`)

#### **cdk.xml** - AWS CDK Development
- **Stack Organization**: Logical nested stack patterns
- **Resource Naming**: Consistent naming conventions
- **Security Best Practices**: IAM, encryption, and access control guidelines
- **Testing Strategy**: Unit testing with Vitest framework
- **Deployment Validation**: CDK synthesis and validation sequences

#### **dotnet.xml** - .NET Framework Guidelines
- Framework-specific development patterns and best practices

#### **terraform.xml** - Infrastructure as Code
- Terraform-specific rules and conventions

### **Sample Prompts** (`cline/sample_prompts/`)

#### **repository-analysis.txt** - Comprehensive Repository Analysis
- **Architecture Mapping**: Complete system structure analysis
- **User Flow Documentation**: End-to-end user journey mapping
- **Data Flow Analysis**: Data sources, transformations, and destinations
- **Integration Analysis**: External dependencies and service mappings
- **Visual Documentation**: Mermaid diagrams for flows and architecture
- **Confidence Assessment**: Structured analysis with confidence ratings

## 🛠️ How to Use with Cline

### **Step 1: Setup Rules in Your Project**

```bash
# Navigate to your project
cd /path/to/your/project

# Create Cline rules directory
mkdir .clinerules

# Copy core generic rules (recommended for all projects)
cp /path/to/agentic-coding-rules-and-templates/cline/.clinerules/generic/* .clinerules/

# Copy framework-specific rules as needed
cp /path/to/agentic-coding-rules-and-templates/cline/.clinerules/frameworks/cdk.xml .clinerules/  # For AWS CDK projects
cp /path/to/agentic-coding-rules-and-templates/cline/.clinerules/frameworks/dotnet.xml .clinerules/  # For .NET projects
```

### **Step 2: Initialize Memory Bank (Optional but Recommended)**

```bash
# Create memory bank directory
mkdir .memory-bank

# Cline will automatically populate this based on the memory-bank.md guidelines
```

### **Step 3: Using Cline with the Rules**

#### **Example 1: Repository Analysis**
```
Hey Cline, I want you to analyze this repository comprehensively. Please use the repository analysis prompt from the sample prompts to understand the architecture, user flows, and data flows.
```

*Cline will automatically:*
- Read the rules from `.clinerules/`
- Apply the systematic analysis framework
- Use confidence assessment (0-10 scale)
- Generate comprehensive documentation in `.cline_docs/repository-analysis.md`
- Create visual diagrams using Mermaid
- Offer to create a memory bank for future sessions

#### **Example 2: Adding a New Feature**
```
I need to add a user authentication system to this React app. Please analyze the current setup and implement it following our development standards.
```

*Cline will:*
- Assess confidence level before starting (analysis.xml)
- Follow development standards (dev-standards.xml)
- Apply systematic investigation checklists
- Implement with proper testing and error handling
- Update memory bank with new patterns learned

#### **Example 3: AWS CDK Infrastructure**
```
Help me create a new CDK stack for a serverless API with DynamoDB backend.
```

*With CDK rules, Cline will:*
- Follow established stack patterns
- Apply security best practices (least privilege, encryption)
- Use consistent naming conventions
- Implement proper testing with Vitest
- Run validation sequence (synth, test, lint)

#### **Example 4: Code Review and Improvement**
```
Please review this component and suggest improvements following our coding standards.
```

*Cline will:*
- Apply dev-standards.xml guidelines
- Assess current code against best practices
- Suggest specific, actionable improvements
- Provide confidence levels for recommendations
- Consider testing and error handling improvements

### **Step 4: Memory Bank Usage**

After initial setup, Cline will maintain context through the memory bank:

```
Update memory bank
```

*This triggers Cline to:*
- Review all memory bank files
- Update current project state
- Document new patterns learned
- Clarify next steps and priorities

## 🎯 Practical Examples

### **Example Project Setup**

```bash
# New React + AWS CDK project
mkdir my-fullstack-app
cd my-fullstack-app

# Setup Cline rules
mkdir .clinerules
cp /path/to/rules/cline/.clinerules/generic/* .clinerules/
cp /path/to/rules/cline/.clinerules/frameworks/cdk.xml .clinerules/

# Initialize with Cline
# In Cline chat:
# "Initialize this project with React frontend and AWS CDK backend, following our established patterns"
```

### **Example Prompts for Different Scenarios**

#### **Starting a New Project**
```
Initialize a new [technology] project following our development standards. Set up the basic structure, testing framework, and development workflow.
```

#### **Analyzing Existing Code**
```
Analyze this codebase using our systematic analysis framework. I need to understand the architecture and identify areas for improvement.
```

#### **Adding Complex Features**
```
I need to implement [feature description]. Please analyze the current system, assess integration points, and implement following our confidence-based approach.
```

#### **Code Review**
```
Review this code against our development standards. Provide specific improvements for code quality, testing, and error handling.
```

## 🔧 Advanced Usage

### **Custom Rules Creation**

You can extend the rules by creating custom XML files in your `.clinerules/` directory:

```xml
<!-- .clinerules/custom-project-rules.xml -->
<custom_rules>
    <project_specific>
        <!-- Your project-specific guidelines -->
    </project_specific>
</custom_rules>
```

### **Team Consistency**

Include `.clinerules/` in version control:

```bash
# Add to .gitignore exceptions
echo "!.clinerules/" >> .gitignore

# Commit rules for team consistency
git add .clinerules/
git commit -m "Add Cline rules for consistent AI-assisted development"
```

### **Memory Bank Maintenance**

Regular memory bank updates ensure context accuracy:

```
# Weekly or after major changes
Update memory bank with recent project developments
```

## 🧪 Testing the Setup

We've created comprehensive test environments for both JavaScript and Python projects:

### **Python Test Environment** (Recommended)
- **Location**: `python-cline-test/` directory
- **Features**: Complete Python project with type hints, pytest, black, flake8, mypy
- **Quick Start**: See `PYTHON_QUICK_START_TESTING.md`

### **JavaScript Test Environment**
- **Location**: `cline-rules-test/` directory  
- **Features**: Basic Node.js project structure
- **Quick Start**: See `QUICK_START_TESTING.md`

### **Test 1: Memory Check (Immediate)**
```
WE CAN DO IT
```
*Expected: Cline should respond with "WE CAN DO IT" confirming rules are loaded*

### **Test 2: Python Code Quality**
```
Add a new function to calculate the average of a list of numbers with proper error handling and tests
```
*Expected: Type hints, comprehensive error handling, unit tests, PEP 8 compliance*

### **Test 3: Confidence Assessment**
```
I want to add a user authentication system. What's your confidence level for implementing this?
```
*Expected: 0-10 scale assessment, clarifying questions about requirements*

### **Test 4: Repository Analysis**
```
Conduct a comprehensive analysis of the python-cline-test project using the repository analysis framework
```
*Expected: Creates comprehensive documentation with Mermaid diagrams*

### **Test 5: Memory Bank Creation**
```
Create a memory bank for this project following the memory-bank.md guidelines
```
*Expected: Creates structured documentation system for context persistence*

## 📊 Benefits

### **For Individual Developers**
- **Consistent Quality**: Enforced coding standards across all AI interactions
- **Risk Reduction**: Confidence assessment prevents breaking changes
- **Knowledge Retention**: Memory bank maintains project context
- **Systematic Approach**: Structured analysis prevents oversight

### **For Teams**
- **Standardization**: Shared rules ensure consistent AI behavior
- **Knowledge Sharing**: Memory bank captures team insights
- **Quality Assurance**: Built-in review and validation processes
- **Onboarding**: New team members get consistent AI assistance

### **For Projects**
- **Maintainability**: Consistent patterns and documentation
- **Reliability**: Systematic testing and error handling
- **Scalability**: Framework-specific best practices
- **Documentation**: Automatic generation of project insights

## 🤝 Contributing

### **Adding New Rules**
1. Create rules in appropriate directory structure
2. Follow existing XML format and documentation standards
3. Include practical examples and usage guidelines
4. Test with real projects before contributing

### **Individual Rules**
See [individuals](individuals) directory for personal rule collections and templates shared by team members.

## 📝 Usage Tips

1. **Start Small**: Begin with generic rules, add framework-specific rules as needed
2. **Customize**: Adapt naming conventions and standards to your project
3. **Version Control**: Include `.clinerules/` in your repository for team consistency
4. **Regular Updates**: Keep memory bank current with project evolution
5. **Test Thoroughly**: Validate AI behavior matches your expectations
6. **Document Patterns**: Capture successful patterns in memory bank for reuse

## 🔍 Troubleshooting

### **Rules Not Being Applied**
- Ensure `.clinerules/` directory is in project root
- Check XML syntax in rule files
- Restart Cline session to reload rules

### **Memory Bank Issues**
- Verify `.memory-bank/` directory structure
- Check file permissions
- Use "update memory bank" command to refresh

### **Confidence Assessment Not Working**
- Ensure `analysis.xml` is in `.clinerules/generic/`
- Ask Cline directly about confidence levels
- Check that investigation checklists are being followed

---

*Transform your AI coding assistant into a systematic, confident development partner with enterprise-grade practices and comprehensive project understanding.*
