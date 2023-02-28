#!/usr/bin/env ruby
# Regular expressin for a phone number

puts ARGV[0].scan(/[0-9]{10}/).join
