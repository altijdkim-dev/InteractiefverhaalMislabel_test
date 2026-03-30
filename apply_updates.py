with open('/Users/kimverhaegh/Desktop/Avans/DesignActivisme/simulatieAlgoritme/index.html', 'r') as f:
    code = f.read()

# 1. Add meter HTML
code = code.replace('<div id="app"></div>\n  <script>',
'''<div id="meterUI" style="position: fixed; left: 30px; top: 50%; transform: translateY(-50%); height: 33vh; width: 100px; display: none; align-items: center; z-index: 1000;">
    <div style="writing-mode: vertical-rl; transform: rotate(180deg); margin-right: 15px; font-weight: bold; font-size: 16px;">diagnose-overtuiging</div>
    <div style="display: flex; flex-direction: column; justify-content: flex-end; width: 40px; height: 100%; border: 2px solid white; background-color: rgba(0,0,0,0.5); position: relative;">
      <div id="meterFill" style="width: 100%; height: 0%; background-color: orange; transition: height 0.5s;"></div>
    </div>
    <div id="meterLabel" style="position: absolute; bottom: -30px; left: 50%; transform: translateX(-50%); font-weight: bold; color: white;">twijfel</div>
  </div>
  <div id="app"></div>
  <script>''')

# 2. Add variables & logic
vardefs = '''    const postsData = {
      'Depressie': ['Depressie tip 1', 'Depressie tip 2', 'Depressie tip 3'],
      'Angst': ['Angst tip 1', 'Angst tip 2', 'Angst tip 3'],
      'OCD': ['OCD tip 1', 'OCD tip 2', 'OCD tip 3'],
      'Stress': ['Stress tip 1', 'Stress tip 2', 'Stress tip 3'],
      'Burnout': ['Burnout tip 1', 'Burnout tip 2', 'Burnout tip 3'],
      'PTSS': ['PTSS tip 1', 'PTSS tip 2', 'PTSS tip 3']
    };

    let foundDokter = false;
    let foundDesc = false;
    let foundEarlySpecial = false;
    let foundFocusSpecial = false;

    function getNegativeEventsCount() {
      return (foundDokter ? 1 : 0) + (foundDesc ? 1 : 0) + (foundEarlySpecial ? 1 : 0) + (foundFocusSpecial ? 1 : 0);
    }

    function updateMeter(totalLikesVal = 0, inFocusMode = false) {
      const meterUI = document.getElementById('meterUI');
      if (!meterUI) return;
      
      let percent = 5 + (totalLikesVal * 20);
      if (inFocusMode) percent += 20;
      percent -= (getNegativeEventsCount() * 20);
      
      if (percent < 0) percent = 0;
      if (percent > 100) percent = 100;
      
      document.getElementById('meterFill').style.height = percent + '%';
      
      let label = 'twijfel';
      if (percent >= 85) label = 'zekerheid';
      else if (percent >= 40) label = 'herkenning';
      document.getElementById('meterLabel').textContent = label;
    }
'''
code = code.replace("    const postsData = {\n      'Depressie': ['Depressie tip 1', 'Depressie tip 2', 'Depressie tip 3'],\n      'Angst': ['Angst tip 1', 'Angst tip 2', 'Angst tip 3'],\n      'OCD': ['OCD tip 1', 'OCD tip 2', 'OCD tip 3'],\n      'Stress': ['Stress tip 1', 'Stress tip 2', 'Stress tip 3'],\n      'Burnout': ['Burnout tip 1', 'Burnout tip 2', 'Burnout tip 3'],\n      'PTSS': ['PTSS tip 1', 'PTSS tip 2', 'PTSS tip 3']\n    };", vardefs)

# 3. Modify sceneFeed startup
code = code.replace("    function sceneFeed(next) {\n      const app = document.getElementById('app');", "    function sceneFeed(next) {\n      document.getElementById('meterUI').style.display = 'flex';\n      updateMeter(0, false);\n      const app = document.getElementById('app');")

# 4. Modify post image
postimg = '''          div.className = 'post';
          div.innerHTML = `<strong><span class="diagnose-tekst">${post.diagnose}</span></strong>
                           <div style="margin-top:10px; margin-bottom:10px; position:relative;">
                             <img src="https://via.placeholder.com/500x500?text=Plaats+hier+je+afbeelding" style="width:100%; height:450px; object-fit:cover;">
                           </div>`;

          const likeImg = document.createElement('img');'''
code = code.replace("          div.className = 'post';\n          div.innerHTML = `<strong><span class=\"diagnose-tekst\">${post.diagnose}</span></strong>`;\n\n          const likeImg = document.createElement('img');", postimg)

# 5. Modify isSpecial onclick
code = code.replace('''                likeImg.src = 'Like_button_clicked.png';
                
                // Tekst laten verschijnen in de post''', '''                likeImg.src = 'Like_button_clicked.png';

                if (!foundFocusSpecial) {
                  foundFocusSpecial = true;
                  updateMeter(totalLikes, focusMode);
                }
                
                // Tekst laten verschijnen in de post''')

# 6. Modify isEarlySpecial onclick
code = code.replace('''                likeImg.src = 'Like_button_clicked.png';
                
                lastScroll = window.scrollY || document.documentElement.scrollTop;''', '''                likeImg.src = 'Like_button_clicked.png';
                
                if (!foundEarlySpecial) {
                  foundEarlySpecial = true;
                  updateMeter(totalLikes, focusMode);
                }
                
                lastScroll = window.scrollY || document.documentElement.scrollTop;''')

# 7. Modify regular onclick
code = code.replace('''                totalLikes++;
                diagnoseLikeCount[post.diagnose]++;
                likeImg.src = 'Like_button_clicked.png';

                setTimeout(() => {''', '''                totalLikes++;
                diagnoseLikeCount[post.diagnose]++;
                likeImg.src = 'Like_button_clicked.png';
                
                updateMeter(totalLikes, focusMode);

                setTimeout(() => {''')

# 8. Modify descDiv onclick
code = code.replace('''            descDiv.onclick = () => {
              // Herstel scrollpositie en ga naar beschrijving
              lastScroll = window.scrollY || document.documentElement.scrollTop;''', '''            descDiv.onclick = () => {
              if (!foundDesc) {
                foundDesc = true;
                updateMeter(totalLikes, focusMode);
              }
              // Herstel scrollpositie en ga naar beschrijving
              lastScroll = window.scrollY || document.documentElement.scrollTop;''')


# 9. Modify sceneStart text sizes & logic
new_start = '''    // Start scene
    function sceneStart(next) {
      document.getElementById('meterUI').style.display = 'none'; // hide in start scene
      const app = document.getElementById('app');
      app.innerHTML = `
        <div style="display: flex; width: 100vw; height: 100vh; position: relative; background-color: #000; overflow: hidden;">
          <!-- Linker helft: Naar de dokter -->
          <div id="btnDokter" style="flex: 1; border-right: 1px solid #333; cursor: pointer; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden;">
             <!-- <img src="URL_A" style="width:100%; height:100%; object-fit:cover; opacity: 0.4;"> -->
             <div style="position: absolute; font-size: 28px; font-weight: bold; color: white; text-align: center; padding: 20px;">Naar de dokter gaan</div>
          </div>
          
          <!-- Rechter helft: Naar sociale media -->
          <div id="btnSocial" style="flex: 1; cursor: pointer; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden;">
             <!-- <img src="URL_B" style="width:100%; height:100%; object-fit:cover; opacity: 0.4;"> -->
             <div style="position: absolute; font-size: 28px; font-weight: bold; color: white; text-align: center; padding: 20px;">Naar sociale media gaan</div>
          </div>

          <!-- Gecentreerde tekst -->
          <div style="position: absolute; top: 0; bottom: 0; left: 50%; transform: translateX(-50%); width: 220px; display: flex; flex-direction: column; justify-content: space-around; align-items: center; text-align: center; pointer-events: none; color: white; background: rgba(0,0,0,0.6); padding: 40px 10px;">
             <div style="font-weight: bold; font-size: 32px; text-transform: uppercase;">Begin verhaal hier</div>
             <div style="font-size: 18px; font-style: italic;">of</div>
             <div style="font-weight: bold; font-size: 18px;">Blijf kritisch kijken<br/>naar wat je ziet,<br/>ook in dit verhaal.</div>
          </div>

          <!-- Popup Dokter -->
          <div id="popupDokter" style="display: none; position: fixed; top: 10%; left: 10%; width: 80%; height: 80%; background-color: white; color: black; z-index: 100; border-radius: 10px; padding: 40px; box-sizing: border-box; box-shadow: 0 0 20px rgba(0,0,0,0.5); text-align: left;">
             <div id="closePopup" style="position: absolute; top: 15px; left: 20px; font-size: 30px; cursor: pointer; font-weight: bold;">&times;</div>
             <h2 style="margin-top: 40px;">Consult bij de dokter</h2>
             <p>Je hebt besloten om naar de dokter te gaan voor professionele hulp. De systemen hier werken buiten de feed en het algoritme om.</p>
          </div>
        </div>
      `;

      document.getElementById('btnDokter').onclick = () => {
        document.getElementById('popupDokter').style.display = 'block';
        if (!foundDokter) {
          foundDokter = true;
          updateMeter(0, false);
        }
      };

      document.getElementById('closePopup').onclick = () => {
        document.getElementById('popupDokter').style.display = 'none';
      };

      document.getElementById('btnSocial').onclick = () => {
        next();
      };
    }'''
scene_start_pattern_start = "    // Start scene"
scene_start_pattern_end = "    // Tweede scene (optioneel)"
code = code[:code.find(scene_start_pattern_start)] + new_start + "\n\n" + code[code.find(scene_start_pattern_end):]

# 10. Router scenes
router = '''    // Branching router & Scenes
    function outcomeRouter(next) {
      document.getElementById('meterUI').style.display = 'none';
      if (getNegativeEventsCount() >= 3) {
        sceneOutcomeTwoPointOne();
      } else {
        sceneOutcomeOnePointOne();
      }
    }

    // --- UITKOMST 1 (0, 1, of 2 negatieve patronen gevonden) ---
    function sceneOutcomeOnePointOne() {
      const app = document.getElementById('app');
      app.innerHTML = `
        <h1 class="titleFeed">Diagnose Feed</h1>
        <div class="post">
          <strong><span class="diagnose-tekst">Diagnose</span></strong>
          <div style="margin-top:10px; margin-bottom:10px; position:relative;">
             <img src="https://via.placeholder.com/500x500?text=Plaats+hier+je+afbeelding" style="width:100%; height:450px; object-fit:cover;">
             <div style="position: absolute; top:70px; bottom:20px; left:20px; right:20px; background:transparent; color:white; display:flex; flex-direction:column; justify-content:center; text-align:center;">
                <h3>Uitkomst 1</h3>
                <p>Je bent relatief onopgemerkt door het algoritme gegleden en nam veel als waarheid aan.</p>
                <p><strong>Scroll omlaag om door te gaan.</strong></p>
             </div>
          </div>
          <img class="like-button-img" src="Like_button.png" style="opacity: 0.5;">
        </div>
        <div style="height: 50vh;"></div>
      `;
      window.scrollTo({top: 0, behavior: 'auto'});
      enableScrollTriggerOutcome(sceneOutcomeOnePointTwo);
    }

    function sceneOutcomeOnePointTwo() {
      const app = document.getElementById('app');
      app.innerHTML = `
        <div style="text-align:center; margin-top:200px;">
          <h2>Resultaat: Tunnelvisie</h2>
          <p>Mede doordat je bijna alles zonder kritiek hebt aangenomen en door bleef klikken, raakte je gevangen in de tunnel.</p>
          <button id="btnNext1" style="margin-top:20px; padding:10px 20px; font-size:16px; cursor:pointer;">Naar Einde</button>
        </div>
      `;
      window.scrollTo({top: 0, behavior: 'auto'});
      document.getElementById('btnNext1').onclick = sceneFinal;
    }

    // --- UITKOMST 2 (3 of 4 negatieve patronen gevonden) ---
    function sceneOutcomeTwoPointOne() {
      const app = document.getElementById('app');
      app.innerHTML = `
        <h1 class="titleFeed" style="color: dodgerblue;">Diagnose Feed</h1>
        <div class="post" style="border-color: dodgerblue;">
          <strong><span class="diagnose-tekst" style="color: dodgerblue;">Diagnose</span></strong>
          <div style="margin-top:10px; margin-bottom:10px; position:relative;">
             <img src="https://via.placeholder.com/500x500?text=Plaats+hier+je+afbeelding" style="width:100%; height:450px; object-fit:cover;">
             <div style="position: absolute; top:70px; bottom:20px; left:20px; right:20px; background:transparent; color:dodgerblue; display:flex; flex-direction:column; justify-content:center; text-align:center;">
                <h3 style="margin-bottom:20px;">Uitkomst 2</h3>
                <p>Je hebt bewust negatieve patronen gevonden en kritische opmerkingen gelezen.</p>
                <p><strong>Scroll omlaag om door te gaan.</strong></p>
             </div>
          </div>
          <img class="like-button-img" src="Like_button.png" style="opacity: 0.5;">
        </div>
        <div style="height: 50vh;"></div>
      `;
      window.scrollTo({top: 0, behavior: 'auto'});
      enableScrollTriggerOutcome(sceneOutcomeTwoPointTwo);
    }

    function sceneOutcomeTwoPointTwo() {
      const app = document.getElementById('app');
      app.innerHTML = `
        <div style="text-align:center; margin-top:200px; color: dodgerblue;">
          <h2>Resultaat: Vrije keuze</h2>
          <p>Doordat je alle verborgen boodschappen hebt ontcijferd, herken je het algoritme en laat je je niet meer zomaar beïnvloeden.</p>
          <button id="btnNext2" style="margin-top:20px; padding:10px 20px; font-size:16px; cursor:pointer; background-color: dodgerblue; color: white; border:none; border-radius: 5px;">Naar Einde</button>
        </div>
      `;
      window.scrollTo({top: 0, behavior: 'auto'});
      document.getElementById('btnNext2').onclick = sceneFinal;
    }

    // Einde
    function sceneFinal() {
      const app = document.getElementById('app');
      document.getElementById('meterUI').style.display = 'none'; // Veiligheid
      app.innerHTML = `
        <div style="text-align:center; margin-top:250px;">
          <h2>Einde van de Simulatie</h2>
          <p>Bedankt voor je deelname. Blijf altijd kritisch kijken naar wat je ziet.</p>
        </div>
      `;
    }

    function enableScrollTriggerOutcome(nextFn) {
      let triggered = false;
      window.onscroll = () => {
        if (triggered) return;
        const scrollTop = window.scrollY || document.documentElement.scrollTop;
        const windowHeight = window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight;
        if (scrollTop + windowHeight >= documentHeight - 5 || scrollTop > 50) {
          triggered = true;
          window.onscroll = null;
          nextFn();
        }
      };
    }
'''

code = code[:code.find("    // Tweede scene (optioneel)")] + router

# 11. Final scenes array
scenes_old = '''    const scenes = [sceneStart, sceneFeed, sceneReflectie];
    let currentScene = 0;
    function nextScene() {
      currentScene++;
      if (currentScene < scenes.length) scenes[currentScene](nextScene);
    }

    // Start
    scenes[0](nextScene);
  </script>'''

scenes_new = '''    const scenes = [sceneStart, sceneFeed, outcomeRouter];
    let currentScene = 0;
    function nextScene() {
      currentScene++;
      if (currentScene < scenes.length) scenes[currentScene](nextScene);
    }

    // Start
    scenes[0](nextScene);
  </script>'''

code = code.replace(scenes_old, scenes_new)

with open('/Users/kimverhaegh/Desktop/Avans/DesignActivisme/simulatieAlgoritme/index.html', 'w') as f:
    f.write(code)
