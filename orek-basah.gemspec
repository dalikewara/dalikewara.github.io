# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name          = "orek-basah"
  spec.version       = "0.1.0"
  spec.authors       = ["dalikewara"]
  spec.email         = ["dalikewara@gmail.com"]

  spec.summary       = ""
  spec.homepage      = ""
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r!^(assets|_layouts|_includes|_sass|LICENSE|README|_config\.yml)!i) }

  spec.add_runtime_dependency "jekyll", "~> 4.2"
end
