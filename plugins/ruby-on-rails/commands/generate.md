---
description: Smart Rails generator with suggestions and best practices
argument-hint: [generator-type] [name] [attributes...]
allowed-tools: Read, Bash(rails:*, bundle:*), Glob
---

Rails generator requested: $ARGUMENTS

First, analyze the request to determine the appropriate Rails generator:

**Available generators:**
- `model` - Create model with attributes (e.g., `model User email:string name:string`)
- `controller` - Create controller with actions (e.g., `controller Users index show`)
- `scaffold` - Full CRUD resource (model, controller, views, routes)
- `migration` - Database migration only
- `resource` - Model, controller, routes (no views)
- `mailer` - Email mailer with views
- `job` - Background job (ActiveJob)
- `channel` - ActionCable channel
- `stimulus` - Stimulus controller

**For the requested generation:**

1. **Validate the request** - Ensure generator type and name follow Rails conventions
2. **Suggest improvements** - Recommend additional attributes, associations, or validations if applicable
3. **Show the command** - Display the exact `rails generate` command before running
4. **Execute the generator** - Run the command and show created files
5. **Post-generation guidance** - Suggest next steps (migrations, routes, tests)

**Rails conventions to follow:**
- Model names: singular, CamelCase (User, BlogPost)
- Controller names: plural, CamelCase (UsersController)
- Table names: plural, snake_case (users, blog_posts)
- Foreign keys: singular_id (user_id)

**Common attribute types:**
- `string` - Short text (varchar)
- `text` - Long text
- `integer` - Whole numbers
- `decimal` - Precise numbers (money)
- `boolean` - True/false
- `datetime` - Date and time
- `references` - Foreign key (belongs_to)
- `jsonb` - JSON data (PostgreSQL)

If no arguments provided, ask what to generate and provide examples.
