Cybersecurity & AI Systems Portfolio

[![GitHub Pages Deployment](https://img.shields.io/badge/deployment-GitHub%20Pages-blue?style=flat-square&logo=github)](https://ms-satti11616.github.io/portfolio2/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Anthropic MCP](https://img.shields.io/badge/Protocol-Anthropic%20MCP-d97706?style=flat-square)](https://modelcontextprotocol.io/)
[![Security Hardened](https://img.shields.io/badge/Security-AST%20Sanitized-critical?style=flat-square)]()

A lightweight, security-hardened personal portfolio and local **Model Context Protocol (MCP)** agent interface deployed over HTTPS via GitHub Pages.


🌐 Live Production

* **Portfolio Endpoint:** [https://ms-satti11616.github.io/portfolio2/](https://ms-satti11616.github.io/portfolio2/)
* **FlyRank Capstone Deliverable:** General AI Fluency Impact Project

🚀 Key Features

 **High-Performance Static Frontend:** Built with pure semantic HTML5 and vanilla CSS3 to achieve sub-100ms load times with zero third-party framework overhead.
 **Launch Hygiene & SEO:** Complete OpenGraph (`og:title`, `og:image`, `og:description`) and Twitter Card metadata for dynamic social sharing previews.
 **Privacy-Preserving Analytics:** Integrated GoatCounter tracking script without cookies or GDPR tracking baggage.
 **Honeypot-Protected Form:** Web3Forms contact routing secured against spam bots via hidden input traps and client-side submission state locking.
 **Local Study & Lab Workspace MCP Agent:** A dedicated Python agent adhering to the Anthropic Model Context Protocol specification for secure, local research indexing.


🛠️ Architecture & MCP Agent Overview

The included `workspace_mcp_agent.py` acts as a local stdio MCP server enabling AI clients (such as Claude Desktop) to search and parse local offensive security lab notes and CTF writeups safely.

 Security & Sandboxing Features:
 **Zero-Token Credential Exposure:** Runs entirely inside the local execution runtime; no API keys or internal notes are sent to cloud storage endpoints.
 **AST Path Containment:** Validates all path parameters using strict regex and root containment logic (`sanitize_path`) to prevent directory traversal (`../../`) attacks.
 **JSON-RPC 2.0 Stdio Dispatcher:** Handles dynamic tool discovery (`tools/list`) and execution (`tools/call`) over standard input/output streams.


## 📂 Repository Structure

```
├── index.html               # Main responsive portfolio interface
├── profile.png              # High-contrast developer avatar
├── workspace_mcp_agent.py   # Standalone Python MCP agent server
└── README.md                # Project documentation

💻 Running the Local MCP Agent
PrerequisitesPython 3.10+Local directory at ~/lab_workspace containing Markdown (.md) research notesSelf-Test & VerificationRun the built-in diagnostic test to verify schema compliance and tool listing:
Bashpython3 workspace_mcp_agent.py --test
Starting the stdio MCP ServerExecute the agent directly for integration with standard MCP hosts:
Bashpython3 workspace_mcp_agent.py
📜 Verified Credentials FeaturedTryHackMe: Cyber Security 101 Learning Path (45h 23m) & Hacker Holidays: Byte Lotus CTF
Mastercard: Cybersecurity Job Simulation (Forage)
EY (Ernst & Young): Forensic & Integrity Services Job Simulation (Forage)
Hasnain Karimain Software House: Python Development Internship (PSEB & Ministry of IT)
Cisco Networking Academy: Introduction to CybersecurityAnthropic Academy:
AI Fluency: Framework & Foundations
👤 Author
Abdul Moiz SattiUndergraduate Researcher in Cybersecurity & AI SystemsGitHub: @Ms-satti11616
