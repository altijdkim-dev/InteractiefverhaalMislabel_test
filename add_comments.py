# Script to add explanatory comments to index.html
with open('/Users/kimverhaegh/Desktop/Avans/DesignActivisme/simulatieAlgoritme/index.html', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. postsData comment
code = code.replace("    const postsData = {", "    // [AANPASSEN: Tekst inhoud] Hier staan de vaste titels/inhoud per diagnose\n    const postsData = {")

# 2. post image
target2 = '''          div.innerHTML = `
             <img src="https://via.placeholder.com/540x675?text=Voltooi+Post+Afbeelding" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit:cover; z-index: 0;">
             <strong style="position: relative; z-index: 1;"><span class="diagnose-tekst">${post.diagnose}</span></strong>
          `;'''
repl2 = '''          div.innerHTML = `
             <!-- [AANPASSEN: Afbeelding] Wijzig de src="..." nar je eigen plaatjes-link voor alle reguliere posts -->
             <img src="https://via.placeholder.com/540x675?text=Voltooi+Post+Afbeelding" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit:cover; z-index: 0;">
             
             <!-- [AANPASSEN: Stijl/Tekst] Dit is de grote witte diagnose-tekst centraal op de post. Pas .diagnose-tekst CSS aan om de look te wijzigen. -->
             <strong style="position: relative; z-index: 1;"><span class="diagnose-tekst">${post.diagnose}</span></strong>
          `;'''
code = code.replace(target2, repl2)

# 3. description comment
code = code.replace("descDiv.textContent = 'Klik hier voor meer informatie';", "// [AANPASSEN: Tekst] De tekst van de doorklik-balk onder willekeurige berichten\n            descDiv.textContent = 'Klik hier voor meer informatie';")

# 4. special post overlay text
target4 = '''                overlayText.innerHTML = `
                  <h3 style="margin-bottom: 20px;">Interactie geregistreerd</h3>
                  <p>Deze speciale interactie heeft de feed beïnvloed.</p>
                  <p><strong>Scroll verder naar beneden om door te gaan.</strong></p>
                `;'''
repl4 = '''                // [AANPASSEN: Tekst & Stijl] Deze text komt tevoorschijn midden op de foto als je op 'Like' klikt bij de speciale post in focus mode
                overlayText.innerHTML = `
                  <h3 style="margin-bottom: 20px;">Interactie geregistreerd</h3>
                  <p>Deze speciale interactie heeft de feed beïnvloed.</p>
                  <p><strong>Scroll verder naar beneden om door te gaan.</strong></p>
                `;'''
code = code.replace(target4, repl4)

# 5. sceneBeschrijving
target5 = '''      app.innerHTML = `
    <div style="text-align:center; margin-top:200px;">
      <h2>Extra informatie</h2>
      <p>Hier staat de verborgen beschrijving die de gebruiker kan lezen.</p>
      <button id="btnGelezen">Gelezen</button>
    </div>
  `;'''
repl5 = '''      // [AANPASSEN: Tekst & HTML] Dit is het scherm dat volgt als je op de willekeurige 'meer informatie' balk in de feed drukt.
      app.innerHTML = `
    <div style="text-align:center; margin-top:200px;">
      <h2>Extra informatie</h2>
      <p>Hier staat de verborgen beschrijving die de gebruiker kan lezen.</p>
      <button id="btnGelezen">Gelezen</button>
    </div>
  `;'''
code = code.replace(target5, repl5)

# 6. sceneSlideshow
target6 = '''      app.innerHTML = `
    <div style="text-align:center; margin-top:50px;">
      <h2>Extra Informatie Slideshow</h2>
      <div class="slideshow-container" id="slideshowContainer">
        <div class="slides-track" id="slidesTrack">
          <div class="slide" style="background-color: #333;">
            <img src="https://via.placeholder.com/400x400?text=Plaats+hier+een+afbeelding" alt="Placeholder">
          </div>
          <div class="slide" style="background-color: #222;">
            <h2>Verdieping</h2>
            <p>Veeg naar links en rechts om tussen de slides te navigeren.</p>
            <p>Hier kun je langere tekst of verdieping kwijt.</p>
          </div>
        </div>
      </div>
      <button id="btnGelezenSlideshow">Gelezen</button>
    </div>
  `;'''
repl6 = '''      // [AANPASSEN: Tekst & Afbeeldingen] Dit is de sleepbare slideshow. Voeg plaatjes of teksten toe in de respectievelijke '.slide' divs
      app.innerHTML = `
    <div style="text-align:center; margin-top:50px;">
      <h2>Extra Informatie Slideshow</h2>
      <div class="slideshow-container" id="slideshowContainer">
        <div class="slides-track" id="slidesTrack">
          <!-- Slide 1 -->
          <div class="slide" style="background-color: #333;">
            <img src="https://via.placeholder.com/400x400?text=Plaats+hier+een+afbeelding" alt="Placeholder">
          </div>
          <!-- Slide 2 -->
          <div class="slide" style="background-color: #222;">
            <h2>Verdieping</h2>
            <p>Veeg naar links en rechts om tussen de slides te navigeren.</p>
            <p>Hier kun je langere tekst of verdieping kwijt.</p>
          </div>
        </div>
      </div>
      <!-- [AANPASSEN: Tekst] Knop om af te sluiten -->
      <button id="btnGelezenSlideshow">Gelezen</button>
    </div>
  `;'''
code = code.replace(target6, repl6)

# 7. sceneStart
target7 = '''app.innerHTML = `
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
          <div style="position: absolute; top: 0; bottom: 0; left: 50%; transform: translateX(-50%); width: 280px; display: flex; flex-direction: column; justify-content: space-around; align-items: center; text-align: center; pointer-events: none; color: white; background: rgba(0,0,0,0.6); padding: 40px 10px;">
             <div style="font-weight: bold; font-size: 42px; text-transform: uppercase;">Begin verhaal hier</div>
             <div style="font-size: 30px; font-style: italic;">of</div>
             <div style="font-weight: bold; font-size: 24px;">Blijf kritisch kijken<br/>naar wat je ziet,<br/>ook in dit verhaal.</div>
          </div>

          <!-- Popup Dokter -->
          <div id="popupDokter" style="display: none; position: fixed; top: 10%; left: 10%; width: 80%; height: 80%; background-color: whitesmoke; color: black; z-index: 100; border-radius: 10px; box-sizing: border-box; box-shadow: 0 0 20px rgba(0,0,0,0.5); text-align: left; overflow: hidden;">
             <div style="display: flex; width: 100%; height: 100%;">
                <div style="flex: 3; padding: 60px; position: relative;">
                   <div id="closePopup" style="position: absolute; top: 15px; left: 20px; font-size: 30px; cursor: pointer; font-weight: bold;">&times;</div>
                   <h2 style="margin-top: 20px; font-size: 32px;">Consult bij de dokter</h2>
                   <p style="font-size: 16pt; line-height: 1.6;">Je hebt besloten om naar de dokter te gaan voor professionele hulp. De systemen hier werken buiten de feed en het algoritme om.</p>
                </div>
                <div style="flex: 1;">
                   <img src="https://via.placeholder.com/300x800?text=Plaats+hier+je+afbeelding" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
             </div>
          </div>
        </div>
      `;'''
repl7 = '''      // [AANPASSEN: Startscherm met grote knoppen en Popups]
      app.innerHTML = `
        <div style="display: flex; width: 100vw; height: 100vh; position: relative; background-color: #000; overflow: hidden;">
          <!-- Linker helft: Naar de dokter -->
          <div id="btnDokter" style="flex: 1; border-right: 1px solid #333; cursor: pointer; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden;">
             <!-- [AANPASSEN: Afbeelding] Om commentaartags weg te halen: verwijder <!-- op begin en -> aan einde, en pas "URL_A" aan. -->
             <!-- <img src="URL_A" style="width:100%; height:100%; object-fit:cover; opacity: 0.4;"> -->
             <div style="position: absolute; font-size: 28px; font-weight: bold; color: white; text-align: center; padding: 20px;">Naar de dokter gaan</div>
          </div>
          
          <!-- Rechter helft: Naar sociale media -->
          <div id="btnSocial" style="flex: 1; cursor: pointer; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden;">
             <!-- [AANPASSEN: Afbeelding] Commentaartags weghalen, "URL_B" vervangen door image link -->
             <!-- <img src="URL_B" style="width:100%; height:100%; object-fit:cover; opacity: 0.4;"> -->
             <div style="position: absolute; font-size: 28px; font-weight: bold; color: white; text-align: center; padding: 20px;">Naar sociale media gaan</div>
          </div>

          <!-- Gecentreerde tekst -->
          <div style="position: absolute; top: 0; bottom: 0; left: 50%; transform: translateX(-50%); width: 280px; display: flex; flex-direction: column; justify-content: space-around; align-items: center; text-align: center; pointer-events: none; color: white; background: rgba(0,0,0,0.6); padding: 40px 10px;">
             <!-- [AANPASSEN: Tekst] De grootte kan je hier in font-size aapassen -->
             <div style="font-weight: bold; font-size: 42px; text-transform: uppercase;">Begin verhaal hier</div>
             <div style="font-size: 30px; font-style: italic;">of</div>
             <div style="font-weight: bold; font-size: 24px;">Blijf kritisch kijken<br/>naar wat je ziet,<br/>ook in dit verhaal.</div>
          </div>

          <!-- Popup Dokter -->
          <div id="popupDokter" style="display: none; position: fixed; top: 10%; left: 10%; width: 80%; height: 80%; background-color: whitesmoke; color: black; z-index: 100; border-radius: 10px; box-sizing: border-box; box-shadow: 0 0 20px rgba(0,0,0,0.5); text-align: left; overflow: hidden;">
             <div style="display: flex; width: 100%; height: 100%;">
                <div style="flex: 3; padding: 60px; position: relative;">
                   <div id="closePopup" style="position: absolute; top: 15px; left: 20px; font-size: 30px; cursor: pointer; font-weight: bold;">&times;</div>
                   <!-- [AANPASSEN: Tekst Dokter Popup] Wijzig de H2 titel en P paragraaf -->
                   <h2 style="margin-top: 20px; font-size: 32px;">Consult bij de dokter</h2>
                   <p style="font-size: 16pt; line-height: 1.6;">Je hebt besloten om naar de dokter te gaan voor professionele hulp. De systemen hier werken buiten de feed en het algoritme om.</p>
                </div>
                <div style="flex: 1;">
                   <!-- [AANPASSEN: Afbeelding Dokter Popup] Plaats in de popup een staande foto door de src hieronder aan te passen -->
                   <img src="https://via.placeholder.com/300x800?text=Plaats+hier+je+afbeelding" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
             </div>
          </div>
        </div>
      `;'''
code = code.replace(target7, repl7)

# 8. Outcomes wrappers
target8 = '''    // --- UITKOMST 1 (0, 1, of 2 negatieve patronen gevonden) ---
    function sceneOutcomeOnePopup() {'''
repl8 = '''    // --- UITKOMST 1 (0, 1, of 2 negatieve patronen gevonden) ---
    // [AANPASSEN: Uitkomst 1 Pop-up] Hier pas je de eerste reactie aan als de gebruiker met stroom meeging.
    function sceneOutcomeOnePopup() {'''
code = code.replace(target8, repl8)

# 9. End Scene
target9 = '''    // Einde
    function sceneFinal() {'''
repl9 = '''    // Einde
    // [AANPASSEN: Eind Scherm] Iedereen komt hier samen. Je kan de teksten hier tweaken.
    function sceneFinal() {'''
code = code.replace(target9, repl9)

with open('/Users/kimverhaegh/Desktop/Avans/DesignActivisme/simulatieAlgoritme/index.html', 'w', encoding='utf-8') as f:
    f.write(code)
