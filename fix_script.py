with open("script.js", "r") as f:
    content = f.read()

content = content.replace("    const finalTimeMs = Date.now() - startTime;", "    const finalTimeMs = startTime ? Date.now() - startTime : 0;")

with open("script.js", "w") as f:
    f.write(content)
