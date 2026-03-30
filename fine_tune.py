with open('/Users/kimverhaegh/Desktop/Avans/DesignActivisme/simulatieAlgoritme/index.html', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update .description background in CSS
code = code.replace('background-color: white;', 'background-color: whitesmoke;')

# 2. Update post image inside updateFeed()
post_image_target = """          div.className = 'post';
          div.innerHTML = `<strong><span class="diagnose-tekst">${post.diagnose}</span></strong>
                           <div style="margin-top:10px; margin-bottom:10px; position:relative;">
                             <img src="https://via.placeholder.com/500x500?text=Plaats+hier+je+afbeelding" style="width:100%; height:450px; object-fit:cover;">
                           </div>`;"""

post_image_replacement = """          div.className = 'post';
          div.style.overflow = 'hidden';
          div.style.border = 'none'; // Geen randje om de foto
          div.style.display = 'flex';
          div.style.flexDirection = 'column';
          div.innerHTML = `
             <img src="https://via.placeholder.com/540x675?text=Voltooi+Post+Afbeelding" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit:cover; z-index: 0;">
             <strong style="position: relative; z-index: 1;"><span class="diagnose-tekst">${post.diagnose}</span></strong>
          `;"""

if post_image_target in code:
    code = code.replace(post_image_target, post_image_replacement)
else:
    print("WARNING: POST IMAGE TARGET NOT FOUND")

# 3. Update sceneStart text and popup sizes
start_scene_target = '''          <!-- Gecentreerde tekst -->
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
          </div>'''

start_scene_replacement = '''          <!-- Gecentreerde tekst -->
          <div style="position: absolute; top: 0; bottom: 0; left: 50%; transform: translateX(-50%); width: 260px; display: flex; flex-direction: column; justify-content: space-around; align-items: center; text-align: center; pointer-events: none; color: white; background: rgba(0,0,0,0.6); padding: 40px 10px;">
             <div style="font-weight: bold; font-size: 42px; text-transform: uppercase;">Begin verhaal hier</div>
             <div style="font-size: 30px; font-style: italic;">of</div>
             <div style="font-weight: bold; font-size: 24px;">Blijf kritisch kijken<br/>naar wat je ziet,<br/>ook in dit verhaal.</div>
          </div>

          <!-- Popup Dokter -->
          <div id="popupDokter" style="display: none; position: fixed; top: 10%; left: 10%; width: 80%; height: 80%; background-color: white; color: black; z-index: 100; border-radius: 10px; box-sizing: border-box; box-shadow: 0 0 20px rgba(0,0,0,0.5); text-align: left; overflow: hidden;">
             <div style="display: flex; width: 100%; height: 100%;">
                <div style="flex: 3; padding: 60px; position: relative;">
                   <div id="closePopup" style="position: absolute; top: 15px; left: 20px; font-size: 30px; cursor: pointer; font-weight: bold;">&times;</div>
                   <h2 style="margin-top: 20px; font-size: 32px;">Consult bij de dokter</h2>
                   <p style="font-size: 16pt; line-height: 1.6;">Je hebt besloten om naar de dokter te gaan voor professionele hulp. De systemen hier werken buiten de feed en het algoritme om.</p>
                </div>
                <div style="flex: 1;">
                   <img src="https://via.placeholder.com/300x800?text=Dokter+Afbeelding" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
             </div>
          </div>'''

if start_scene_target in code:
    code = code.replace(start_scene_target, start_scene_replacement)
else:
    print("WARNING: START SCENE TARGET NOT FOUND")

# 4. Replace outcome scenes with Popups
router_target = '''    // Branching router & Scenes
    function outcomeRouter(next) {'''

import re
match = re.search(r"    // Branching router & Scenes\n    function outcomeRouter.*?{", code)
if match:
    code_up_to_router = code[:match.start()]

    router_replacement = '''    // Branching router & Scenes
    function outcomeRouter() {
      // Bepaal de uitkomst en roep de bijbehorende popup (Scene 1) aan
      if (getNegativeEventsCount() >= 3) {
        sceneOutcomeTwoPopup();
      } else {
        sceneOutcomeOnePopup();
      }
    }

    // --- UITKOMST 1 (0, 1, of 2 negatieve patronen gevonden) ---
    function sceneOutcomeOnePopup() {
      const app = document.getElementById('app');
      app.innerHTML = `
        <div style="position: fixed; top:0; left:0; right:0; bottom:0; background: rgba(0,0,0,0.8); display:flex; align-items:center; justify-content:center; z-index:2000;">
          <div style="position: relative; width: 80%; height: 80%; border-radius: 10px; overflow: hidden; background-color: #222; box-shadow: 0 0 20px rgba(0,0,0,0.8);">
            <!-- Full height popup background image -->
            <img src="https://via.placeholder.com/800x600?text=Achtergrond+Afbeelding" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit:cover; opacity: 0.3; z-index: 1;">
            
            <div id="closeOutcomePopup" style="position: absolute; top: 15px; right: 20px; font-size: 30px; cursor: pointer; font-weight: bold; color: white; z-index: 3;">&times;</div>
            
            <div style="position: relative; z-index: 2; padding: 60px; text-align: center; color: white; height: 100%; display: flex; flex-direction: column; justify-content: center;">
              <h2 style="font-size: 36px; margin-bottom: 20px;">Uitkomst 1</h2>
              <p style="font-size: 16pt; line-height: 1.6;">Je bent relatief onopgemerkt door het algoritme gegleden en nam veel als waarheid aan.</p>
            </div>
          </div>
        </div>
      `;
      window.scrollTo({top: 0, behavior: 'auto'});
      
      document.getElementById('closeOutcomePopup').onclick = () => {
        sceneOutcomeOnePointTwo(); // Naar Scene 2
      };
    }

    function sceneOutcomeOnePointTwo() {
      const app = document.getElementById('app');
      app.innerHTML = `
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; text-align:center;">
          <h2>Resultaat: Tunnelvisie</h2>
          <p style="font-size: 16pt; max-width: 600px; margin-bottom: 40px;">Mede doordat je bijna alles zonder kritiek hebt aangenomen en door bleef klikken, raakte je gevangen in de tunnel.</p>
          <button id="btnNext1" style="padding:10px 20px; font-size:16px; cursor:pointer;">Naar Einde</button>
        </div>
      `;
      window.scrollTo({top: 0, behavior: 'auto'});
      document.getElementById('btnNext1').onclick = sceneFinal;
    }

    // --- UITKOMST 2 (3 of 4 negatieve patronen gevonden) ---
    function sceneOutcomeTwoPopup() {
      const app = document.getElementById('app');
      app.innerHTML = `
        <div style="position: fixed; top:0; left:0; right:0; bottom:0; background: rgba(0,0,0,0.8); display:flex; align-items:center; justify-content:center; z-index:2000;">
          <div style="position: relative; width: 80%; height: 80%; border-radius: 10px; overflow: hidden; background-color: #222; box-shadow: 0 0 20px rgba(0,0,0,0.8);">
            <!-- Full height popup background image -->
            <img src="https://via.placeholder.com/800x600?text=Achtergrond+Afbeelding" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit:cover; opacity: 0.3; z-index: 1;">
            
            <div id="closeOutcomePopup2" style="position: absolute; top: 15px; right: 20px; font-size: 30px; cursor: pointer; font-weight: bold; color: dodgerblue; z-index: 3;">&times;</div>
            
            <div style="position: relative; z-index: 2; padding: 60px; text-align: center; color: dodgerblue; height: 100%; display: flex; flex-direction: column; justify-content: center;">
              <h2 style="font-size: 36px; margin-bottom: 20px;">Uitkomst 2</h2>
              <p style="font-size: 16pt; line-height: 1.6;">Je hebt bewust negatieve patronen gevonden en kritische opmerkingen gelezen.</p>
            </div>
          </div>
        </div>
      `;
      window.scrollTo({top: 0, behavior: 'auto'});
      
      document.getElementById('closeOutcomePopup2').onclick = () => {
        sceneOutcomeTwoPointTwo(); // Naar Scene 2
      };
    }

    function sceneOutcomeTwoPointTwo() {
      const app = document.getElementById('app');
      app.innerHTML = `
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; text-align:center; color: dodgerblue;">
          <h2>Resultaat: Vrije keuze</h2>
          <p style="font-size: 16pt; max-width: 600px; margin-bottom: 40px;">Doordat je alle verborgen boodschappen hebt ontcijferd, herken je het algoritme en laat je je niet meer zomaar beïnvloeden.</p>
          <button id="btnNext2" style="padding:10px 20px; font-size:16px; cursor:pointer; background-color: dodgerblue; color: white; border:none; border-radius: 5px;">Naar Einde</button>
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
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; text-align:center;">
          <h2>Einde van de Simulatie</h2>
          <p style="font-size: 16pt;">Bedankt voor je deelname. Blijf altijd kritisch kijken naar wat je ziet.</p>
        </div>
      `;
    }'''

    scene_array_tail = '''
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
'''
    code = code_up_to_router + router_replacement + scene_array_tail
else:
    print("WARNING: ROUTER SCENES TARGET NOT FOUND")

# Z-index repair on like button just to be safe
code = code.replace("likeImg.className = 'like-button-img';", "likeImg.className = 'like-button-img';\n          likeImg.style.zIndex = '1';")


with open('/Users/kimverhaegh/Desktop/Avans/DesignActivisme/simulatieAlgoritme/index.html', 'w', encoding='utf-8') as f:
    f.write(code)
