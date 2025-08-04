# Intentionally insecure security group
resource "aws_security_group" "open_all" {
  name        = "open-all"
  description = "Allow everything"
  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]  # BAD: open to the world
  }
}

