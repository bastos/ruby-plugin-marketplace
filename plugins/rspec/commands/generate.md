---
description: Generate RSpec spec file for a Ruby class, module, or Rails component
argument-hint: "<class_name or file_path>"
allowed-tools: ["Read", "Write", "Glob", "Bash"]
---

# Generate RSpec Spec

Create a new spec file for a given class, module, or Rails component.

## Arguments

The user provides either:
- **Class/module name**: `User`, `OrderProcessor`, `Api::V1::UsersController`
- **File path**: `app/models/user.rb`, `app/services/order_processor.rb`

## Generation Strategy

### 1. Locate Source File
Find the source file to understand the class structure:
```ruby
# From class name: User -> app/models/user.rb
# From path: use directly
```

### 2. Analyze Class
Read the source to identify:
- Class/module name
- Public methods
- Associations (for ActiveRecord)
- Validations (for models)
- Before actions (for controllers)

### 3. Generate Spec
Create spec file in corresponding location:
```
app/models/user.rb          -> spec/models/user_spec.rb
app/services/foo/bar.rb     -> spec/services/foo/bar_spec.rb
app/controllers/users_controller.rb -> spec/requests/users_spec.rb
lib/my_gem/parser.rb        -> spec/lib/my_gem/parser_spec.rb
```

## Spec Templates

### Model Spec
```ruby
RSpec.describe User, type: :model do
  describe "validations" do
    # Based on model validations
  end

  describe "associations" do
    # Based on model associations
  end

  describe "#method_name" do
    it "description" do
      pending "Add spec"
    end
  end
end
```

### Service Spec
```ruby
RSpec.describe OrderProcessor do
  describe "#call" do
    context "with valid input" do
      it "processes successfully" do
        pending "Add spec"
      end
    end

    context "with invalid input" do
      it "returns error" do
        pending "Add spec"
      end
    end
  end
end
```

### Request Spec (for controllers)
```ruby
RSpec.describe "Users", type: :request do
  describe "GET /users" do
    it "returns success" do
      get users_path
      expect(response).to have_http_status(:ok)
    end
  end
end
```

## Best Practices

- Use `describe` for the class/method
- Use `context` for different scenarios
- Include both happy path and error cases
- Add pending placeholders for methods
- Use factories with `let` blocks
- Follow project's existing spec patterns

## Examples

```
/rspec:generate User
/rspec:generate app/models/user.rb
/rspec:generate OrderProcessor
/rspec:generate Api::V1::UsersController
```
