# 🏠 RealtorsPk Automation

## BDD-Based Real Estate Test Automation Framework

RealtorsPk Automation is a structured automation testing project built to validate critical real estate application workflows using **Behavior-Driven Development (BDD)** principles.

The framework combines business-readable feature scenarios with reusable page objects, step definitions, test data, utilities, assertions, and reporting to provide reliable regression coverage for RealtorsPk.

---

## 🎯 Project Objectives

The automation project aims to:

- Automate critical real estate workflows
- Reduce repetitive manual regression
- Improve test coverage
- Detect application regressions earlier
- Keep scenarios readable for business and QA teams
- Build reusable automation components
- Generate screenshots and reports
- Support end-to-end testing
- Prepare automation for CI/CD integration

---

# 🧪 Automation Scope

The automation suite can validate:

- Application launch
- Registration
- Authentication
- Login
- Logout
- Home page
- Property search
- Property filters
- Property listings
- Property details
- Buy/Rent selection
- Location search
- Price filtering
- Property type filtering
- Favorites
- Saved properties
- Customer inquiries
- Contact agent
- Profile management
- Navigation
- Forms
- Validation messages
- Error handling

---

# 🥒 BDD Architecture

The project follows a BDD-oriented automation flow:

```text
Business Requirement
        ↓
Feature File
        ↓
Scenario
        ↓
Step Definitions
        ↓
Page Object
        ↓
Reusable Actions
        ↓
Application UI
        ↓
Assertions
        ↓
Report / Screenshot
```

This approach separates business behavior from implementation details.

---

# 📁 Recommended Project Structure

```text
RealtorsPk/
│
├── features/
│   ├── authentication.feature
│   ├── property-search.feature
│   ├── property-listing.feature
│   ├── inquiry.feature
│   └── profile.feature
│
├── step-definitions/
│   ├── auth.steps
│   ├── search.steps
│   ├── listing.steps
│   └── inquiry.steps
│
├── pages/
│   ├── LoginPage
│   ├── HomePage
│   ├── SearchPage
│   ├── PropertyPage
│   ├── InquiryPage
│   └── ProfilePage
│
├── locators/
│
├── utilities/
│
├── test-data/
│
├── config/
│
├── reports/
│
├── screenshots/
│
├── logs/
│
└── README.md
```

Use the actual repository folder names where they already exist.

---

# 📝 Feature Files

Feature files should describe application behavior in business-readable language.

Example:

```gherkin
Feature: User Login

  Scenario: Login with valid credentials
    Given the user is on the RealtorsPk login page
    When the user enters valid credentials
    And clicks the login button
    Then the user should be redirected to the dashboard
```

---

# 🔍 Property Search BDD Scenario

```gherkin
Feature: Property Search

  Scenario: Search available properties in Islamabad
    Given the user is on the property search screen
    When the user selects "Islamabad"
    And selects "For Sale"
    And applies the required price range
    Then relevant property listings should be displayed
```

---

# 🏘 Property Details Scenario

```gherkin
Feature: Property Details

  Scenario: View selected property information
    Given property search results are displayed
    When the user selects a property
    Then the property details should display
    And the property price should be visible
    And the location should be visible
    And contact information should be available
```

---

# 📩 Property Inquiry Scenario

```gherkin
Feature: Property Inquiry

  Scenario: Submit inquiry for a property
    Given the user is viewing a property
    When the user selects contact agent
    And enters valid inquiry details
    And submits the inquiry
    Then a confirmation message should be displayed
```

---

# 🧩 Step Definitions

Step definitions connect BDD scenarios with automation implementation.

Example structure:

```text
Given user is on Login page
        ↓
LoginPage.open()

When user enters valid credentials
        ↓
LoginPage.login()

Then dashboard should appear
        ↓
DashboardPage.verifyLoaded()
```

Keep step definitions small and reusable.

---

# 🏗 Page Object Model

Use page objects to separate application locators and actions from test scenarios.

Example:

```text
SearchPage
├── openSearch()
├── selectCity()
├── selectPropertyType()
├── enterPriceRange()
├── applyFilters()
└── verifyResults()
```

Feature files should never contain locator implementation details.

---

# ♻️ Reusable Components

Reusable actions may include:

```text
loginUser()
searchProperty()
applyFilters()
openProperty()
submitInquiry()
logoutUser()
```

Reuse common behavior instead of duplicating automation code.

---

# 🔖 BDD Tags

Use tags to organize execution.

Example:

```gherkin
@smoke
@login
Scenario: Valid user login
```

Recommended tags:

```text
@smoke
@sanity
@regression
@login
@search
@listing
@inquiry
@profile
@negative
@critical
@e2e
```

---

# 🚦 Smoke Testing

Smoke suite should cover critical functionality:

```text
Launch Application
      ↓
Login
      ↓
Search Property
      ↓
Open Property
      ↓
Submit Inquiry
      ↓
Logout
```

---

# 🔄 Regression Testing

Regression coverage may include:

- Authentication
- Search
- Filters
- Listings
- Property details
- Favorites
- Inquiries
- Profile
- Navigation
- Validation
- Negative scenarios

---

# ❌ Negative Testing

Validate scenarios such as:

- Invalid login credentials
- Empty required fields
- Invalid email
- Invalid phone
- No property results
- Invalid price range
- Missing inquiry information
- Unauthorized actions

Every negative scenario must validate the expected application behavior.

---

# ✅ Assertions

Every test should contain meaningful assertions.

Examples:

```text
Login successful
Property results displayed
Correct city shown
Property details displayed
Inquiry successfully submitted
Expected validation shown
```

Avoid tests that only perform clicks without validating results.

---

# 🎯 Locator Strategy

Prefer stable locators:

```text
Test ID
Accessibility ID
Stable ID
Semantic Locator
CSS Selector
XPath only when necessary
```

Avoid:

- Long dynamic XPath
- Screen coordinates
- Index-based selectors
- Highly fragile selectors

---

# 📊 Test Data

Keep test data separate.

Suggested structure:

```text
test-data/
├── users
├── properties
├── searches
├── inquiries
└── invalid-data
```

Example data:

```text
User
City
Property Type
Minimum Price
Maximum Price
Inquiry Message
Expected Result
```

---

# ⚙️ Configuration

Maintain configuration independently.

Example:

```text
config/
├── local
├── qa
└── staging
```

Configuration can include:

```text
Base URL
Environment
Username
Timeout
Browser / Device
Screenshot Path
Report Path
```

---

# ⏳ Synchronization

Avoid unnecessary hard waits.

Prefer:

```text
Wait until visible
Wait until enabled
Wait until results loaded
Wait until navigation completes
```

This improves test stability.

---

# 📸 Screenshots

Capture screenshots automatically when scenarios fail.

Suggested structure:

```text
screenshots/
├── failed/
└── execution-date/
```

Example:

```text
property_search_no_results_failed.png
```

---

# 📊 Reporting

Reports should include:

- Feature name
- Scenario
- Execution status
- Duration
- Passed scenarios
- Failed scenarios
- Failure reason
- Screenshots
- Logs

BDD reports should make scenario results easy to understand.

---

# 📝 Logging

Example:

```text
INFO Feature started: Property Search
INFO Selected city: Islamabad
INFO Applied property filter
INFO Search results displayed
PASS Property Search scenario
```

Sensitive credentials must never be logged.

---

# 🔄 Failure Handling

```text
Scenario Failure
       ↓
Capture Screenshot
       ↓
Collect Logs
       ↓
Record Failure
       ↓
Attach Evidence
       ↓
Mark Scenario Failed
```

---

# 🧪 Test Independence

Each scenario should be independently executable where practical.

Avoid:

```text
Scenario B requires Scenario A.
```

Prefer independent setup and test data.

---

# 💻 VS Code Workflow

```text
Clone Repository
      ↓
Open in VS Code
      ↓
Install Dependencies
      ↓
Configure Environment
      ↓
Run BDD Tests
      ↓
Review Reports
```

Repository:

```text
https://github.com/haroondhanyal/RealtorsPk
```

---

# 🔄 CI/CD Ready Flow

```text
Code Commit
    ↓
Install Dependencies
    ↓
Run Smoke Tags
    ↓
Run Regression Tags
    ↓
Generate BDD Report
    ↓
Publish Evidence
```

Possible platforms:

- GitHub Actions
- Jenkins
- Azure DevOps
- Bitbucket Pipelines

---

# 🚀 Future Enhancements

The automation framework can later support:

- API automation
- API + UI combined testing
- Data-driven BDD
- Parallel execution
- Cross-browser validation
- Mobile automation
- Database validation
- CI/CD pipelines
- Advanced HTML reporting
- Visual testing
- Automated test-data creation
- Scheduled regression

---

# ⭐ Automation Best Practices

- Write business-readable scenarios
- Keep feature files simple
- Reuse step definitions
- Keep locators outside feature files
- Use reusable page objects
- Avoid duplicated automation
- Use meaningful assertions
- Keep scenarios independent
- Avoid unnecessary hard waits
- Generate evidence on failure

---

# 🔄 Complete Automation Journey

```text
User Opens RealtorsPk
        ↓
Login
        ↓
Search Property
        ↓
Apply Filters
        ↓
Review Listings
        ↓
Open Property
        ↓
Save / Contact Agent
        ↓
Submit Inquiry
        ↓
Validate Confirmation
        ↓
Logout
```

---

# 🎯 Final Goal

RealtorsPk Automation provides a maintainable BDD-based regression framework for validating important real estate workflows.

The framework combines:

**BDD Feature Files → Step Definitions → Page Objects → Reusable Actions → Assertions → Reports**

to help QA teams reduce regression effort, improve test readability, detect defects earlier, and deliver more reliable RealtorsPk releases.
