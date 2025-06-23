# Testing Guide for Agentic Coding Rules and Templates

This guide will help you test the setup and functionality of the agentic coding rules with Cline.

## 🧪 Test Setup Instructions

### Prerequisites
1. Have Cline installed and running
2. Have this repository cloned locally
3. Have a test project ready (or we'll create one)

### Test Environment Setup

```bash
# Create a test project directory
mkdir cline-rules-test
cd cline-rules-test

# Initialize basic project structure
mkdir src tests docs
touch src/index.js tests/index.test.js package.json

# Setup Cline rules
mkdir .clinerules
cp ../agentic-coding-rules-and-templates/cline/.clinerules/generic/* .clinerules/

# Create basic package.json for testing
echo '{
  "name": "cline-rules-test",
  "version": "1.0.0",
  "description": "Test project for Cline rules",
  "main": "src/index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  }
}' > package.json
```

## 🔬 Test Cases

### Test 1: Rule Recognition and Memory Check
**Purpose**: Verify Cline recognizes and loads the rules

**Test Command**:
```
WE CAN DO IT
```

**Expected Result**: 
- Cline should respond with "WE CAN DO IT" (this is the memory check from agent-rules.xml)
- This confirms the rules are loaded and being followed

### Test 2: Confidence Assessment Framework
**Purpose**: Test the systematic analysis framework

**Test Command**:
```
I want to add a new API endpoint to handle user registration. What's your confidence level for implementing this?
```

**Expected Behavior**:
- Cline should ask for confidence assessment details
- Should reference the 0-10 confidence scale
- Should ask clarifying questions about:
  - Business rules
  - Database impact
  - Integration effects
  - Security implications
- Should not proceed until confidence is 8+ or gaps are addressed

### Test 3: Development Standards Application
**Purpose**: Verify dev-standards.xml is being followed

**Test Command**:
```
Write a simple user authentication function with proper error handling and testing
```

**Expected Behavior**:
- Should create clean, modular code
- Should include comprehensive error handling
- Should write unit tests
- Should follow functional programming patterns
- Should include minimal but meaningful logging
- Should avoid code duplication

### Test 4: Repository Analysis
**Purpose**: Test the comprehensive analysis prompt

**Test Command**:
```
Conduct a comprehensive analysis of this test project using the repository analysis framework from the sample prompts.
```

**Expected Behavior**:
- Should create `.cline_docs/repository-analysis.md`
- Should include confidence assessments for each component
- Should generate Mermaid diagrams
- Should offer to create memory bank structure
- Should follow the systematic analysis framework

### Test 5: Memory Bank Creation
**Purpose**: Test memory bank functionality

**Test Command**:
```
Create a memory bank for this project following the memory-bank.md guidelines
```

**Expected Behavior**:
- Should create `.memory-bank/` directory
- Should create core files: projectbrief.md, productContext.md, etc.
- Should populate files with relevant project information
- Should establish the hierarchical structure

### Test 6: Framework-Specific Rules (if applicable)
**Purpose**: Test framework-specific rule application

**Setup**: Copy CDK rules if testing AWS CDK
```bash
cp ../agentic-coding-rules-and-templates/cline/.clinerules/frameworks/cdk.xml .clinerules/
```

**Test Command**:
```
Help me create a simple CDK stack for a Lambda function
```

**Expected Behavior**:
- Should follow CDK-specific patterns
- Should apply security best practices
- Should use consistent naming conventions
- Should include proper testing setup
- Should run validation sequence

## 📊 Test Results Checklist

### ✅ Basic Functionality
- [ ] Rules are loaded and recognized
- [ ] Memory check responds correctly
- [ ] Confidence assessment framework is applied
- [ ] Development standards are followed

### ✅ Advanced Features
- [ ] Repository analysis generates comprehensive documentation
- [ ] Memory bank structure is created correctly
- [ ] Framework-specific rules are applied when present
- [ ] Mermaid diagrams are generated with proper formatting

### ✅ Quality Assurance
- [ ] Code generated follows clean coding principles
- [ ] Unit tests are comprehensive and well-structured
- [ ] Error handling is defensive and appropriate
- [ ] Logging follows security guidelines

### ✅ Documentation
- [ ] Analysis documentation is thorough and structured
- [ ] Confidence levels are clearly stated
- [ ] Knowledge gaps are identified and addressed
- [ ] Memory bank maintains project context

## 🐛 Troubleshooting Common Issues

### Issue: Rules Not Being Applied
**Symptoms**: Cline doesn't follow the expected patterns
**Solutions**:
1. Check `.clinerules/` directory is in project root
2. Verify XML files are valid (no syntax errors)
3. Restart Cline session
4. Check file permissions

### Issue: Memory Check Fails
**Symptoms**: Cline doesn't respond with "WE CAN DO IT"
**Solutions**:
1. Verify `agent-rules.xml` is in `.clinerules/generic/`
2. Check XML syntax in agent-rules.xml
3. Restart Cline and try again

### Issue: Confidence Assessment Not Working
**Symptoms**: Cline proceeds without confidence assessment
**Solutions**:
1. Ensure `analysis.xml` is present
2. Ask explicitly: "What's your confidence level for this task?"
3. Check that investigation checklists are being referenced

### Issue: Memory Bank Not Created
**Symptoms**: `.memory-bank/` directory not created or populated
**Solutions**:
1. Verify `memory-bank.md` is in `.clinerules/generic/`
2. Ask explicitly to create memory bank
3. Check directory permissions

## 📈 Success Metrics

### Quantitative Measures
- **Rule Compliance**: 100% of expected behaviors should be observed
- **Response Time**: Cline should respond appropriately within normal timeframes
- **Documentation Quality**: Generated docs should be comprehensive and well-structured

### Qualitative Measures
- **Code Quality**: Generated code should be clean, testable, and maintainable
- **Analysis Depth**: Repository analysis should provide meaningful insights
- **Context Retention**: Memory bank should capture and maintain relevant project information

## 🎯 Next Steps After Testing

### If Tests Pass
1. **Deploy to Real Projects**: Copy rules to actual development projects
2. **Team Rollout**: Share setup instructions with team members
3. **Customize Rules**: Adapt rules for specific project needs
4. **Monitor Usage**: Track how rules improve development workflow

### If Tests Fail
1. **Debug Issues**: Use troubleshooting guide to identify problems
2. **Check Setup**: Verify all files are in correct locations
3. **Validate XML**: Ensure rule files have valid XML syntax
4. **Seek Support**: Document issues and seek help from repository maintainers

## 📝 Test Report Template

```markdown
# Cline Rules Test Report

**Date**: [Date]
**Tester**: [Name]
**Environment**: [OS, Cline version, etc.]

## Test Results Summary
- **Total Tests**: 6
- **Passed**: [X]/6
- **Failed**: [X]/6
- **Overall Success Rate**: [X]%

## Detailed Results
### Test 1: Rule Recognition
- Status: [Pass/Fail]
- Notes: [Observations]

### Test 2: Confidence Assessment
- Status: [Pass/Fail]
- Notes: [Observations]

[Continue for all tests...]

## Issues Encountered
[List any issues and their resolutions]

## Recommendations
[Suggestions for improvements or next steps]
```

---

Use this guide to systematically test the agentic coding rules setup and ensure everything works as expected before deploying to production projects.
