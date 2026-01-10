---
description: Benchmark Ruby code for performance comparison and profiling
argument-hint: "[file or code block]"
allowed-tools: ["Bash", "Read", "Write", "Glob"]
---

# Benchmark Ruby Code

Profile and compare Ruby code performance.

## Arguments

The user may provide:
- **File path**: Run benchmarks defined in a file
- **Code description**: Generate a benchmark comparing implementations
- **No argument**: Analyze current context for optimization opportunities

## Execution Strategy

### Quick Benchmark

For simple timing:

```ruby
require "benchmark"

time = Benchmark.measure do
  # Code to benchmark
end

puts time
```

### Comparative Benchmark with benchmark-ips

```ruby
require "benchmark/ips"

Benchmark.ips do |x|
  x.config(warmup: 2, time: 5)

  x.report("implementation A") do
    # First implementation
  end

  x.report("implementation B") do
    # Second implementation
  end

  x.compare!
end
```

### Memory Profiling

```ruby
require "memory_profiler"

report = MemoryProfiler.report do
  # Code to analyze
end

report.pretty_print
```

### CPU Profiling

```ruby
require "stackprof"

StackProf.run(mode: :cpu, out: "tmp/stackprof.dump") do
  # Code to profile
end

# Then analyze with:
# stackprof tmp/stackprof.dump --text
```

## Benchmark File Template

When creating a benchmark file:

```ruby
#!/usr/bin/env ruby
# frozen_string_literal: true

require "bundler/setup"
require "benchmark/ips"
require_relative "../lib/my_gem"

# Setup data
data = Array.new(1000) { rand(100) }

Benchmark.ips do |x|
  x.config(warmup: 2, time: 5)

  x.report("Array#each") do
    result = []
    data.each { |n| result << n * 2 }
  end

  x.report("Array#map") do
    data.map { |n| n * 2 }
  end

  x.compare!
end
```

## Common Benchmarks

### String Operations

```ruby
Benchmark.ips do |x|
  x.report("interpolation") { "Hello, #{name}!" }
  x.report("concatenation") { "Hello, " + name + "!" }
  x.report("format") { format("Hello, %s!", name) }
  x.compare!
end
```

### Collection Operations

```ruby
Benchmark.ips do |x|
  x.report("each + push") do
    result = []
    items.each { |i| result.push(i * 2) }
  end

  x.report("map") { items.map { |i| i * 2 } }

  x.compare!
end
```

### Hash vs Array Lookup

```ruby
array = (1..1000).to_a
hash = array.to_h { |n| [n, true] }
set = Set.new(array)

Benchmark.ips do |x|
  x.report("Array#include?") { array.include?(500) }
  x.report("Hash#key?") { hash.key?(500) }
  x.report("Set#include?") { set.include?(500) }
  x.compare!
end
```

## Output Interpretation

Explain benchmark results:
- **i/s**: Iterations per second (higher is better)
- **± percentage**: Standard deviation (lower means more consistent)
- **comparison**: How much faster/slower vs baseline

## Dependencies Check

Before running benchmarks, check for required gems:

```bash
# Check for benchmark-ips
bundle info benchmark-ips 2>/dev/null || echo "Add 'gem benchmark-ips' to Gemfile"

# Check for memory_profiler
bundle info memory_profiler 2>/dev/null || echo "Add 'gem memory_profiler' to Gemfile"

# Check for stackprof
bundle info stackprof 2>/dev/null || echo "Add 'gem stackprof' to Gemfile"
```

## Examples

```
/ruby:benchmark                              # Suggest optimizations for current code
/ruby:benchmark benchmarks/array_ops.rb      # Run benchmark file
/ruby:benchmark "map vs each for filtering"  # Generate comparison benchmark
```
