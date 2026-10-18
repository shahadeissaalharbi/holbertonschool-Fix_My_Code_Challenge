#!/usr/bin/env ruby

# Sort integer arguments (ascending), ignoring non-integers
result = []

ARGV.each do |arg|
  # skip anything that is not an integer
  next unless arg =~ /^-?\d+$/

  result << arg.to_i
end

# sort numerically (not as strings)
result.sort.each do |number|
  puts number
end
