with open('/Users/kimverhaegh/Desktop/Avans/DesignActivisme/simulatieAlgoritme/index.html', 'a') as f:
    f.write('''
    const scenes = [sceneStart, sceneFeed, outcomeRouter];
    let currentScene = 0;
    function nextScene() {
      currentScene++;
      if (currentScene < scenes.length) scenes[currentScene](nextScene);
    }

    // Start
    scenes[0](nextScene);
  </script>
</body>
</html>
''')
