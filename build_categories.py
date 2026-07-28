import os
import json
import random

# Directory setup
BASE_DIR = r"C:\Users\lajit\.gemini\antigravity\scratch\sivakasi-fireworks-authority"
CAT_DIR = os.path.join(BASE_DIR, "category")
os.makedirs(CAT_DIR, exist_ok=True)

# Shared HTML components
SHARED_HEADER = """
<header class="site-header" id="siteHeader">
  <div class="header-inner container">
    <a href="/index.html" class="logo" aria-label="Sivakasi Fireworks Guide Home">
      <span class="logo-icon">🎆</span>
      <span class="logo-text">Sivakasi<strong>Fireworks</strong></span>
    </a>
    <nav class="main-nav" id="mainNav" aria-label="Main navigation">
      <ul class="nav-list">
        <li><a href="/index.html">Home</a></li>
        <li><a href="/crackers-buying-guide.html">Buying Guide</a></li>
        <li><a href="/safety-guide.html">Safety</a></li>
        <li><a href="/fireworks-types.html">Types</a></li>
        <li><a href="/festival-guide.html">Festival Guide</a></li>
        <li><a href="/blog/index.html">Blog</a></li>
        <li><a href="/faq.html">FAQ</a></li>
      </ul>
    </nav>
    <div class="header-actions">
      <button class="search-toggle" id="searchToggle" aria-label="Open search">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
      </button>
      <button class="hamburger" id="hamburger" aria-label="Toggle mobile menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
  <div class="search-bar" id="searchBar" aria-hidden="true">
    <div class="container">
      <input type="search" placeholder="Search fireworks guides, safety tips..." id="siteSearch" aria-label="Search">
      <button onclick="document.getElementById('searchBar').classList.remove('open')" aria-label="Close search">✕</button>
    </div>
  </div>
</header>
"""

SHARED_FOOTER = """
<footer class="site-footer">
  <div class="footer-inner container">
    <div class="footer-brand">
      <div class="footer-logo">🎆 Sivakasi<strong>Fireworks</strong></div>
      <p>India's most trusted fireworks education platform. Your complete guide to Sivakasi crackers, Diwali celebrations, and festival safety.</p>
      <div class="footer-social">
        <a href="#" aria-label="Facebook">f</a>
        <a href="#" aria-label="Instagram">in</a>
        <a href="#" aria-label="YouTube">▶</a>
      </div>
    </div>
    <div class="footer-links">
      <div class="footer-col">
        <h4>Guides</h4>
        <ul>
          <li><a href="/crackers-buying-guide.html">Buying Guide</a></li>
          <li><a href="/safety-guide.html">Safety Guide</a></li>
          <li><a href="/fireworks-types.html">Fireworks Types</a></li>
          <li><a href="/kids-safety.html">Kids Safety</a></li>
          <li><a href="/festival-guide.html">Festival Guide</a></li>
          <li><a href="/festival-checklist.html">Festival Checklist</a></li>
          <li><a href="/shipping-guide.html">Shipping Guide</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Categories</h4>
        <ul>
          <li><a href="/category/rockets.html">Rockets</a></li>
          <li><a href="/category/sparklers.html">Sparklers</a></li>
          <li><a href="/category/fancy-fireworks.html">Fancy Fireworks</a></li>
          <li><a href="/category/gift-boxes.html">Gift Boxes</a></li>
          <li><a href="/category/kids-crackers.html">Kids Crackers</a></li>
          <li><a href="/category/premium-collection.html">Premium Collection</a></li>
          <li><a href="/category/festival-packs.html">Festival Packs</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <ul>
          <li><a href="/about.html">About Us</a></li>
          <li><a href="/author/index.html">Our Authors</a></li>
          <li><a href="/contact.html">Contact</a></li>
          <li><a href="/blog/index.html">Blog</a></li>
          <li><a href="/faq.html">FAQ</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Legal</h4>
        <ul>
          <li><a href="/privacy-policy.html">Privacy Policy</a></li>
          <li><a href="/terms-of-service.html">Terms of Service</a></li>
          <li><a href="/disclaimer.html">Disclaimer</a></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="container">
      <p>© 2025 SivakasiFireworks.in — All Rights Reserved. Educational content only. Always follow local laws when purchasing and using fireworks.</p>
    </div>
  </div>
</footer>
"""

ORG_SCHEMA = {
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Sivakasi Fireworks Guide",
  "url": "https://sivakasi-fireworks.in",
  "logo": "https://sivakasi-fireworks.in/images/logo.png",
  "description": "India's most trusted educational platform for Sivakasi fireworks, Diwali celebrations, and festival safety guides.",
  "sameAs": ["https://redcrackers.net"]
}

categories = [
    {
        "slug": "rockets",
        "title": "Rocket Fireworks | Buy Sivakasi Sky Rockets Online – Guide & Price",
        "desc": "Complete guide to rocket fireworks — types, safety, buying tips, price ranges, and the best Sivakasi rockets for Diwali celebrations.",
        "h1": "Rocket Fireworks — The Sky's the Limit",
        "color": "#1e3a8a",
        "icon": "🚀",
        "specific_desc": "Rocket fireworks have always been the crown jewel of any Diwali celebration. From the classic single rockets that shoot straight up with a satisfying whoosh, to advanced multi-shot rockets that paint the night sky with vibrant colors, there is a rocket for every enthusiast. Whistling rockets add an auditory thrill, while ground rockets provide a unique, low-altitude display. Understanding the different varieties allows you to curate the perfect aerial show for your family.",
        "physics": "At their core, rockets rely on basic physics. A black powder charge provides the thrust necessary for lift-off, stabilized by a carefully balanced wooden stick. Once the rocket reaches its apex, a secondary time-delay fuse ignites the 'payload' or 'burst charge,' creating the spectacular visual and acoustic effects. The quality of chemicals used dictates the vividness of the colors and the height achieved.",
        "items": ["Baby Rockets", "Whistling Rockets", "Colour Smoke Rockets", "Double Burst Rockets", "Parachute Rockets", "Premium Sky Rockets"],
        "tips": ["Always check the stick straightness before buying.", "Ensure the fuse is intact and safely covered.", "Opt for multi-burst rockets for better value.", "Verify the manufacturing date to ensure the powder is fresh.", "Look for standard safety certifications on the box."],
        "safety": ["Always use a stable launch tube or heavy bottle.", "Never hold a lit rocket in your hand.", "Ensure a clear overhead launch zone free of trees.", "Keep a bucket of water nearby.", "Never try to relight a dud rocket."]
    },
    {
        "slug": "fancy-fireworks",
        "title": "Fancy Fireworks | Premium Sivakasi Fancy Crackers Guide & Buying Tips",
        "desc": "Complete guide to fancy fireworks from Sivakasi — peacocks, helicopters, butterflies, sky shots, and more. Expert buying tips and safety advice.",
        "h1": "Fancy Fireworks — Spectacular Shows Every Time",
        "color": "#7c3aed",
        "icon": "✨",
        "specific_desc": "Fancy fireworks represent the artistic side of the Sivakasi pyrotechnic industry. These aren't just loud bangs; they are choreographed visual experiences. The category encompasses beautiful ground spinners like the Peacock, aerial novelties like Helicopters and Butterflies, and mesmerizing fountains like Golden Rain. These fireworks are specifically designed to prioritize visual effects, emitting showers of sparks, glowing shapes, and changing colors that captivate audiences of all ages.",
        "physics": "The magic of fancy fireworks lies in the precise layering of chemical compositions. Different metallic salts are pressed into tubes in specific sequences to create changing colors—strontium for red, barium for green, and copper for blue. Novelty shapes like helicopters use angled thrust ports to generate both lift and spin simultaneously, creating a beautiful spiral effect as they ascend.",
        "items": ["Peacock Feathers", "Flying Helicopters", "Magic Butterflies", "Colour Changing Spinners", "Golden Rain Fountains", "Musical Crackers"],
        "tips": ["Choose items based on your available space (ground vs aerial).", "Look for 'smokeless' varieties for better visual clarity.", "Buy assorted packs to get a variety of effects.", "Check for moisture damage on the cardboard tubes.", "Premium fancy items often have thicker, more durable bases."],
        "safety": ["Place fancy aerial items on a flat, solid surface.", "Do not lean over the firework when lighting.", "Maintain at least 15 feet of distance.", "Keep away from dry grass and flammable materials.", "Wait 15 minutes before approaching spent fireworks."]
    },
    {
        "slug": "flower-pots",
        "title": "Flower Pots Fireworks | Sivakasi Fountain Crackers Guide 2025",
        "desc": "Everything about flower pot fireworks — how they work, types, safety, buying guide, and the best Sivakasi flower pots for Diwali and family celebrations.",
        "h1": "Flower Pots & Fountain Fireworks",
        "color": "#059669",
        "icon": "🌋",
        "specific_desc": "Flower pots, also known as fountains, are a staple of Indian festivals. From small pots suitable for tight spaces to massive conical fountains that erupt into a 15-foot shower of gold and silver sparks, they are beloved for their stunning, continuous displays. Color-changing varieties and those that crackle add layers of excitement. They are widely considered one of the safest fireworks, making them perfect for family celebrations and younger participants (aged 8+).",
        "physics": "A flower pot is essentially a cone-shaped tube packed tightly with a pyrotechnic mixture. As it burns from top to bottom, the increasing surface area of the cone means more powder burns simultaneously, causing the shower of sparks to grow taller and wider. The sparks are typically created by coarse metal powders like iron or titanium burning in the air.",
        "items": ["Mini Flower Pots", "Asoka Flower Pots", "Colour Changing Pots", "Crackling Fountains", "Giant Silver Pots", "Multi-Effect Cones"],
        "tips": ["Bigger cones equal taller and longer-lasting displays.", "Check the base to ensure it sits perfectly flat.", "Look for 'crackling' variants for an auditory bonus.", "Buy in bulk boxes for the best per-piece value.", "Avoid pots with loose powder leaking from the top."],
        "safety": ["Place only on flat, paved surfaces, never on grass.", "Light the tip at arm's length using an agarbatti or sparkler.", "Never hold a flower pot while it is burning.", "Keep a safe distance of at least 10 feet.", "Do not try to reignite if it stops halfway."]
    },
    {
        "slug": "ground-chakkars",
        "title": "Ground Chakkars | Spinning Wheel Fireworks Guide – Sivakasi",
        "desc": "Complete guide to ground chakkars (spinning wheel fireworks) — how they work, types, safety rules, buying tips, and best Sivakasi chakkars for Diwali.",
        "h1": "Ground Chakkars — Mesmerizing Spinning Fireworks",
        "color": "#ea580c",
        "icon": "🌀",
        "specific_desc": "Ground chakkars are the traditional spinning wheels of light that define Diwali nights. Ranging from small standard chakkars to massive 'big' or 'special' chakkars, they create a mesmerizing vortex of golden sparks. Some advanced variations incorporate color-changing cores or crackling finales. Because they stay on the ground and don't produce loud explosions, they are a favorite among children and families looking for safe, beautiful visual displays.",
        "physics": "The physics of a ground chakkar is an elegant display of action and reaction. A coiled tube is filled with a fast-burning powder mixture. A small hole on the side of the casing acts as an exhaust port. When lit, the escaping gases generate thrust, causing the entire firework to spin rapidly on its central axis, spraying sparks outward in a circular pattern due to centrifugal force.",
        "items": ["Normal Chakkars", "Big Zamin Chakkars", "Special Crackling Chakkars", "Colour Chakkars", "Deluxe Wheel Chakkars", "Wire Chakkars"],
        "tips": ["Ensure the center pivot or base is perfectly flat.", "Buy larger chakkars for a wider, longer-lasting spin.", "Look for tightly wound coils without cracks.", "Store them flat to maintain their balance.", "Color chakkars offer a great modern twist on the classic."],
        "safety": ["Use only on a completely smooth, hard surface (concrete/tiles).", "Keep feet and loose clothing well away from the spinning radius.", "Light them at arm's length and step back immediately.", "Never attempt to pick up a spinning chakkar.", "Wait for the casing to cool down before disposal."]
    },
    {
        "slug": "sparklers",
        "title": "Sparklers Online | Best Sivakasi Sparklers for Diwali & All Occasions",
        "desc": "Complete sparklers guide — electric sparklers, wire sparklers, color sparklers, lollipop sparklers. Buying tips, safety rules, and best sparklers from Sivakasi.",
        "h1": "Sparklers — Light Up Every Celebration",
        "color": "#ca8a04",
        "icon": "🎇",
        "specific_desc": "Sparklers are the universal symbol of celebration. From standard 10cm wire sparklers to massive 50cm variants, they bring joy to Diwali, weddings, and birthdays alike. The classic 'electric' sparklers provide a brilliant white shower, while color sparklers (red, green, gold) add variety. Lollipop sparklers and root sparklers offer thicker, longer-lasting burns. They are the perfect entry-level firework for children (under close supervision) to participate in the festivities safely.",
        "physics": "Sparklers consist of a stiff wire core coated in a thick paste of pyrotechnic composition. This paste contains a fuel, an oxidizer, and metal powders (like aluminum, iron, or titanium) that create the iconic branching sparks when they burn in the air. A binder holds it all together. The slow, controlled burn rate allows for a sustained, hand-held display.",
        "items": ["10cm Electric Sparklers", "15cm Colour Sparklers", "30cm Crackling Sparklers", "50cm Jumbo Sparklers", "Lollipop Sparklers", "Root Sparklers"],
        "tips": ["Buy longer sparklers (30cm+) for younger children to keep the sparks away from hands.", "Store in a perfectly dry place; damp sparklers will not light.", "Thicker coatings usually mean a longer burn time.", "Electric (white) sparklers typically burn brighter than color ones.", "Always check the wire quality—it shouldn't bend easily."],
        "safety": ["Hold the sparkler at arm's length, away from the face and body.", "Only light one sparkler at a time.", "Never wave them aggressively near other people.", "Wear closed-toe shoes to protect feet from falling sparks.", "Immediately drop spent wires into a bucket of water or sand."]
    },
    {
        "slug": "gift-boxes",
        "title": "Fireworks Gift Boxes | Sivakasi Crackers Combo Packs & Gift Sets",
        "desc": "Complete guide to fireworks gift boxes and combo packs — what's inside, how to choose the right pack for your budget, and best Sivakasi gift box options.",
        "h1": "Fireworks Gift Boxes — Everything in One Box",
        "color": "#c8102e",
        "icon": "🎁",
        "specific_desc": "Fireworks gift boxes are the ultimate convenient solution for festival shopping. Ranging from small ₹500 assortment packs to massive ₹5000+ premium trunks, these boxes take the guesswork out of buying. They are beautifully packaged and contain a curated mix of sparklers, chakkars, flower pots, fountains, and small aerial items. They make perfect corporate gifts, family presents, and are an excellent way to ensure you have a balanced variety of fireworks for your celebration.",
        "physics": "The 'physics' of a gift box is all about balance and logistics. Manufacturers carefully select items that complement each other, ensuring a mix of ground effects, aerial displays, and low-noise items. The packaging is designed to prevent shifting and friction during transport, maximizing safety while presenting the fireworks in an appealing, organized manner.",
        "items": ["Mini Assortment Box (20 Items)", "Standard Family Gift Box", "Premium Gifting Trunk", "Kids Special Combo Box", "Corporate Gifting Pack", "Mega Festival Bonanza Box"],
        "tips": ["Check the itemized list on the back of the box before buying.", "Avoid boxes that look crushed or damaged on the corners.", "Ensure the box has a good mix of ground and aerial fireworks.", "Compare the individual item cost vs. the box price to check value.", "Look for boxes tailored to your needs (e.g., Kids Special)."],
        "safety": ["Store the entire box in a cool, dry place away from heat sources.", "Do not open the box near open flames or lit fireworks.", "Keep the box closed when not actively selecting a firework.", "Ensure individual items haven't been damaged in transit.", "Follow the specific safety instructions for each item inside."]
    },
    {
        "slug": "bombs",
        "title": "Atom Bombs & Sound Crackers | Sivakasi Bomb Crackers Guide",
        "desc": "Complete guide to atom bombs and sound crackers from Sivakasi — types, sound levels, safety rules, and buying tips.",
        "h1": "Atom Bombs & Sound Crackers",
        "color": "#1a1a2e",
        "icon": "💣",
        "specific_desc": "For many, the thrill of Diwali is incomplete without the resonant boom of sound crackers. This category includes the classic Atom Bombs, Hydrogen Bombs, Bullet Bombs, and newer eco-friendly sound varieties. While they provide a visceral, percussive experience, they require the utmost respect and strict adherence to safety and legal guidelines. Understanding decibel (dB) limits and safe usage distances is crucial when incorporating these into your festival plans.",
        "physics": "Sound crackers rely on confinement to generate a loud noise. A highly reactive flash powder is tightly wrapped in layers of strong paper and twine. When the fuse ignites the powder, the rapid production of gases creates immense internal pressure. When the casing finally ruptures, it creates a powerful shockwave in the air, which we perceive as a loud 'bang.'",
        "items": ["Classic Atom Bomb", "Hydrogen Bomb", "Bullet Bomb", "King Kong Bomb", "Eco-Friendly Sound Bomb", "Paper Bomb"],
        "tips": ["Always check the decibel (dB) rating on the packaging.", "Ensure the fuse is long enough for a safe retreat.", "Buy from reputed brands that adhere to legal noise limits.", "Look for tightly bound, heavy casing for consistent performance.", "Consider green/eco-alternatives that produce less smoke."],
        "safety": ["Never light a bomb while holding it in your hand.", "Maintain a strict safety radius of at least 20 feet.", "Do not cover bombs with tin cans, glass, or heavy objects.", "Avoid using sound crackers near hospitals or animal shelters.", "If a bomb fails to detonate, soak it in water after waiting 20 minutes."]
    },
    {
        "slug": "garlands",
        "title": "Garland Crackers | Serial Cracker Strings – Sivakasi Guide & Buying Tips",
        "desc": "Complete guide to garland crackers and serial strings from Sivakasi — lengths, types, safety tips, and buying guide for Diwali celebrations.",
        "h1": "Garland Crackers — The Classic Festival String",
        "color": "#7f1d1d",
        "icon": "📿",
        "specific_desc": "Garland crackers, or serial strings (walas), are the heartbeat of grand celebrations, political victories, and massive festival events. Ranging from modest 50-shot strings to monumental 10,000-shot 'mega-garlands,' they provide a prolonged, rhythmic sequence of explosions. They symbolize prosperity, ward off evil spirits in traditional beliefs, and create an unmistakable atmosphere of joyous chaos that defines major Indian street celebrations.",
        "physics": "A garland cracker is essentially a series of small firecrackers connected by a single, fast-burning master fuse. The speed of the master fuse is carefully calibrated. As it burns down the line, it ignites the individual cracker fuses in rapid succession. The interconnected nature means that one continuous burn dictates the timing and rhythm of the entire sequence.",
        "items": ["100-Shot Garland", "1000-Shot Mega String", "5000-Shot Celebration Wala", "Colour Peony String", "Crackling Garland", "Mini Serial Crackers"],
        "tips": ["Choose the length based on your available outdoor space.", "Check the thickness and continuity of the main master fuse.", "Thicker individual crackers usually mean a louder overall sound.", "Buy boxed garlands rather than loose ones to prevent tangling.", "Green cracker varieties offer reduced smoke during long burns."],
        "safety": ["Always unroll the entire garland flat on the ground before lighting.", "Never attempt to hold or hang a garland while it is firing.", "Keep a massive distance, as these strings can jump and twist unpredictably.", "Ensure the firing area is clear of vehicles and dry vegetation.", "Sweep up paper debris immediately after to prevent smoldering fires."]
    },
    {
        "slug": "kids-crackers",
        "title": "Kids Crackers | Safe Sivakasi Fireworks for Children – Complete Guide",
        "desc": "Safe fireworks for children — sparklers, butterfly crackers, flower pots, and more. Age-appropriate guide with safety rules for parents and kids.",
        "h1": "Kids Crackers — Safe Fun for the Little Ones",
        "color": "#db2777",
        "icon": "🎈",
        "specific_desc": "Introducing children to the magic of fireworks is a cherished festival tradition, but safety must always come first. The Kids Crackers category focuses entirely on low-impact, low-noise, and high-visual items designed for children aged 5 to 12 (always with adult supervision). This includes items like sparklers, magic snakes, pop-its, small flower pots, and ground chakkars. The goal is to provide a magical, sensory experience without the terrifying loud noises or unpredictable movements of larger fireworks.",
        "physics": "Kids' fireworks typically rely on slower-burning chemical compositions and avoid tight confinement. By eliminating explosive flash powder, these items produce gentle showers of sparks, glowing shapes, or expanding carbon ash (like the magic snake) rather than shockwaves. They are engineered to be predictable, operating consistently within a small, controlled radius.",
        "items": ["Magic Snakes", "Party Poppers", "Lollipop Sparklers", "Mini Ground Chakkars", "Twinkling Stars", "Butterfly Spinners"],
        "tips": ["Prioritize visual effects and strictly avoid loud noise makers.", "Look for long-handled items (like 30cm sparklers) to keep heat away from bodies.", "Buy items with clear age recommendations on the box.", "Select smokeless or 'green' varieties to protect sensitive lungs.", "Invest in safety glasses as a fun, protective accessory."],
        "safety": ["Adult supervision is mandatory at all times—no exceptions.", "Dress kids in well-fitting cotton clothes; avoid loose synthetics.", "Teach them to light items at arm's length and step back.", "Enforce a 'one at a time' rule for lighting.", "Have a bucket of water and a first-aid kit readily accessible."]
    },
    {
        "slug": "premium-collection",
        "title": "Premium Fireworks Collection | High-End Sivakasi Crackers & Sky Shots",
        "desc": "Premium fireworks collection — high-end sky shots, multi-shot cakes, display fireworks, and luxury crackers from Sivakasi. Guide for spectacular shows.",
        "h1": "Premium Fireworks Collection — For Show-Stopping Displays",
        "color": "#0f172a",
        "icon": "👑",
        "specific_desc": "For those who want to turn their Diwali into a professional-grade pyrotechnic show, the Premium Collection is the answer. This category features high-end multi-shot cakes (ranging from 30 to 240 shots), massive 3.5-inch sky shells, and intricate display pieces that paint the entire sky. These items are the pinnacle of Sivakasi craftsmanship, offering choreographed sequences of brocade crowns, weeping willows, and thunderous salutes that rival municipal fireworks displays.",
        "physics": "Premium multi-shot cakes are complex engineering marvels. They consist of dozens of heavy cardboard tubes fused together in sequence. Inside each tube is a lifting charge, a time-delay fuse, and a specialized payload shell. The master fuse connects them all, utilizing varying fuse lengths to control the pace of the barrage, firing multiple shells simultaneously or in rapid succession to create layered aerial artistry.",
        "items": ["60-Shot Multi-Colour Cake", "120-Shot Rapid Barrage", "3.5 Inch Sky Shells", "Brocade Crown Display", "Weeping Willow Effects", "Premium Show-Stopper Box"],
        "tips": ["Plan your display area; these require massive overhead clearance.", "Look for heavy, sturdy boxes that won't tip over when firing.", "Read the effect descriptions to choreograph a diverse show.", "Check the total duration of the multi-shot cake for value.", "Buy from premium Sivakasi brands for reliable ignition and bright colors."],
        "safety": ["Place multi-shot cakes on perfectly level, hard ground.", "Brace cakes with bricks or sandbags to prevent tipping.", "Maintain a safety radius of at least 50-100 feet depending on the item.", "Never ever lean over a multi-shot cake, even if it appears dud.", "Spectators should remain seated well away from the firing zone."]
    },
    {
        "slug": "festival-packs",
        "title": "Festival Packs | Complete Sivakasi Fireworks Packages for Every Occasion",
        "desc": "Festival fireworks packs and combo deals from Sivakasi — Diwali packs, family packs, budget packs, premium packs. Everything you need in one purchase.",
        "h1": "Festival Fireworks Packs — Complete Celebration in One Order",
        "color": "#0d9488",
        "icon": "🎊",
        "specific_desc": "Festival Packs are the ultimate convenience for holiday planners. Whether you are hosting an intimate family gathering or a massive neighborhood block party, these pre-configured packages provide a perfectly balanced assortment of fireworks. Ranging from budget-friendly options to all-inclusive mega-deals, Festival Packs ensure you have the right mix of sparklers for the kids, ground effects for the evening, and aerial displays for the grand finale, all coordinated into a single, cost-effective purchase.",
        "physics": "The design of a Festival Pack revolves around the 'arc of celebration.' Curators build these packs by balancing different pyrotechnic physics—mixing the slow-burn chemistry of sparklers and fountains with the rapid-expansion physics of small aerials and the percussive shockwaves of minor sound crackers. This provides a diverse sensory experience spanning light, color, motion, and sound.",
        "items": ["Budget Diwali Pack (₹1000)", "Family Joy Combo (₹2500)", "Premium Block Party Pack (₹5000)", "Green Crackers Eco-Pack", "Kids Safe Celebration Kit", "Grand Finale Assortment"],
        "tips": ["Assess your audience before buying (e.g., more kids means less loud crackers).", "Compare the contents against buying items individually to ensure good value.", "Look for packs that highlight 'Green Crackers' for eco-conscious celebrations.", "Order well in advance to avoid last-minute stock shortages.", "Check if the pack includes essential lighting tools like long incense sticks."],
        "safety": ["Unpack the combo box in a safe, dry location before the event.", "Sort items by type and age-appropriateness before starting.", "Designate one sober adult as the 'Master of Ceremonies' to handle lighting.", "Keep the main stash of fireworks away from the active lighting zone.", "Have a clear timeline and safety plan for the evening's display."]
    }
]

def generate_html(cat):
    # Dynamic related categories (pick 4 excluding current)
    other_cats = [c for c in categories if c['slug'] != cat['slug']]
    random.seed(cat['slug']) # consistent randomness
    rel_cats = random.sample(other_cats, 4)
    
    rel_cats_html = ""
    for rc in rel_cats:
        rel_cats_html += f'''
        <div class="category-card" style="border-top: 4px solid {rc['color']}">
            <div class="card-icon">{rc['icon']}</div>
            <h3><a href="/category/{rc['slug']}.html">{rc['h1'].split('—')[0].strip()}</a></h3>
            <p>{rc['desc'][:80]}...</p>
        </div>'''
        
    products_html = ""
    prices = ["₹150 - ₹300", "₹250 - ₹500", "₹400 - ₹800", "₹50 - ₹150", "₹600 - ₹1200", "₹900 - ₹2000"]
    safety_ratings = ["High (Age 8+)", "Medium (Age 12+)", "Adult Supervision", "High (Age 5+)", "Adult Only", "Medium"]
    for i, item in enumerate(cat['items']):
        price = prices[i % len(prices)]
        s_rate = safety_ratings[i % len(safety_ratings)]
        products_html += f'''
        <div class="product-card">
            <h4>{item}</h4>
            <p>Premium quality {cat['slug'].replace('-', ' ')} sourced directly from Sivakasi.</p>
            <div class="product-meta">
                <span class="price-range">Price: {price}</span>
                <span class="safety-badge">Safety: {s_rate}</span>
            </div>
        </div>'''

    tips_html = "".join([f"<li>{tip}</li>" for tip in cat['tips']])
    safety_html = "".join([f"<li>{s}</li>" for s in cat['safety']])
    
    faqs = [
        {"q": f"Are {cat['slug'].replace('-', ' ')} safe for kids?", "a": f"When used according to guidelines and with strict adult supervision, many items in the {cat['slug'].replace('-', ' ')} category are safe. Always check the age rating on the box."},
        {"q": f"How should I store leftover {cat['slug'].replace('-', ' ')}?", "a": "Store them in a cool, dry place away from direct sunlight, moisture, and any sources of heat or open flame. Keep them tightly sealed in their original boxes."},
        {"q": f"Where can I buy genuine Sivakasi {cat['slug'].replace('-', ' ')}?", "a": "For the best quality, we recommend checking out authorized dealers like RedCrackers.net to ensure you get authentic Sivakasi products."},
        {"q": f"Do {cat['slug'].replace('-', ' ')} have an expiry date?", "a": "While fireworks don't exactly 'expire', their performance degrades over time, especially if exposed to humidity. It's best to use them within 1-2 years of manufacture."},
        {"q": f"What is the standard price for good quality {cat['slug'].replace('-', ' ')}?", "a": "Prices vary widely based on size and effects. Generally, authentic Sivakasi products offer the best value for money due to their superior chemical compositions and safety standards."}
    ]
    
    faqs_html = ""
    faq_schema = []
    for f in faqs:
        faqs_html += f'''
        <details class="faq-item">
            <summary>{f['q']}</summary>
            <p>{f['a']}</p>
        </details>'''
        faq_schema.append({
            "@type": "Question",
            "name": f['q'],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": f['a']
            }
        })
        
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            ORG_SCHEMA,
            {
                "@type": "WebPage",
                "@id": f"https://sivakasi-fireworks.in/category/{cat['slug']}.html",
                "url": f"https://sivakasi-fireworks.in/category/{cat['slug']}.html",
                "name": cat['title'],
                "description": cat['desc']
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://sivakasi-fireworks.in/index.html"},
                    {"@type": "ListItem", "position": 2, "name": "Categories", "item": "https://sivakasi-fireworks.in/fireworks-types.html"},
                    {"@type": "ListItem", "position": 3, "name": cat['h1'].split('—')[0].strip(), "item": f"https://sivakasi-fireworks.in/category/{cat['slug']}.html"}
                ]
            },
            {
                "@type": "FAQPage",
                "mainEntity": faq_schema
            }
        ]
    }
    
    schema_json = json.dumps(schema, indent=2)

    html = f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{cat['title']}</title>
    <meta name="description" content="{cat['desc']}">
    <link rel="canonical" href="https://sivakasi-fireworks.in/category/{cat['slug']}.html">
    
    <meta property="og:title" content="{cat['title']}">
    <meta property="og:description" content="{cat['desc']}">
    <meta property="og:url" content="https://sivakasi-fireworks.in/category/{cat['slug']}.html">
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://sivakasi-fireworks.in/images/og-{cat['slug']}.jpg">
    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{cat['title']}">
    <meta name="twitter:description" content="{cat['desc']}">
    <meta name="twitter:image" content="https://sivakasi-fireworks.in/images/og-{cat['slug']}.jpg">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    
    <link rel="stylesheet" href="/css/style.css">
    
    <script type="application/ld+json">
    {schema_json}
    </script>
    
    <style>
        .category-hero {{
            background: linear-gradient(135deg, {cat['color']} 0%, #0f0f0f 100%);
            color: white;
            padding: 80px 20px;
            text-align: center;
        }}
        .category-hero .icon {{
            font-size: 4rem;
            margin-bottom: 20px;
            display: inline-block;
        }}
        .category-hero h1 {{
            font-family: 'Outfit', sans-serif;
            font-size: 3rem;
            margin-bottom: 15px;
        }}
        .category-hero p.subtitle {{
            font-size: 1.2rem;
            opacity: 0.9;
            max-width: 600px;
            margin: 0 auto;
        }}
        .content-section {{
            padding: 60px 20px;
        }}
        .grid-cards {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }}
        .product-card, .category-card, .blog-card {{
            background: #fff;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        }}
        .cta-box {{
            background: #f8f9fa;
            border-left: 5px solid {cat['color']};
            padding: 30px;
            margin: 40px 0;
            border-radius: 0 12px 12px 0;
        }}
        .breadcrumbs {{
            padding: 15px 20px;
            background: #f0f0f0;
            font-size: 0.9rem;
        }}
        .breadcrumbs a {{ color: #1a1a1a; text-decoration: none; }}
        .faq-item {{
            margin-bottom: 15px;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            padding: 15px;
        }}
        .faq-item summary {{
            font-weight: 600;
            cursor: pointer;
            font-family: 'Outfit', sans-serif;
        }}
        .faq-item p {{ margin-top: 10px; color: #4b5563; }}
        .internal-links a {{ margin-right: 15px; display: inline-block; color: {cat['color']}; font-weight: 500; }}
    </style>
</head>
<body>
    {SHARED_HEADER}
    
    <div class="breadcrumbs container">
        <a href="/index.html">Home</a> &gt; 
        <a href="/fireworks-types.html">Categories</a> &gt; 
        <strong>{cat['h1'].split('—')[0].strip()}</strong>
    </div>

    <section class="category-hero">
        <div class="container">
            <span class="icon">{cat['icon']}</span>
            <h1>{cat['h1']}</h1>
            <p class="subtitle">{cat['desc']}</p>
        </div>
    </section>

    <main class="container content-section">
        <article class="category-description">
            <h2>About {cat['h1'].split('—')[0].strip()}</h2>
            <p>{cat['specific_desc']}</p>
            <p>{cat['physics']}</p>
            <p>Choosing the right fireworks is essential for a memorable festival. For the best quality, we recommend checking out authorized dealers like <a href="https://redcrackers.net" target="_blank" rel="noopener">RedCrackers.net</a>, the Official RedCrackers Website, to ensure you are getting authentic, properly tested Sivakasi products. Our guide helps you understand exactly what you're buying so you can plan the ultimate celebration safely and efficiently.</p>
        </article>

        <section class="buying-tips mt-5">
            <h2>What to Look For When Buying</h2>
            <ul>
                {tips_html}
            </ul>
        </section>

        <section class="popular-products mt-5">
            <h2>Popular Products in This Category</h2>
            <div class="grid-cards">
                {products_html}
            </div>
        </section>

        <section class="safety-rules mt-5">
            <h2>Safety Tips for {cat['h1'].split('—')[0].strip()}</h2>
            <ul>
                {safety_html}
            </ul>
        </section>

        <div class="cta-box">
            <h3>Ready to plan your Diwali purchases?</h3>
            <p>Check out our comprehensive <a href="/crackers-buying-guide.html">Fireworks Buying Guide</a> to learn how to identify authentic Sivakasi brands, understand pricing, and build the perfect festival checklist.</p>
        </div>

        <section class="related-categories mt-5">
            <h2>Explore Related Categories</h2>
            <div class="grid-cards">
                {rel_cats_html}
            </div>
        </section>

        <section class="related-articles mt-5">
            <h2>Related Articles</h2>
            <div class="grid-cards">
                <div class="blog-card">
                    <h3><a href="/blog/diwali-preparation-guide.html">Ultimate Diwali Preparation Guide</a></h3>
                    <p>Get ready for the festival of lights with our step-by-step checklist.</p>
                </div>
                <div class="blog-card">
                    <h3><a href="/blog/green-crackers-explained.html">Green Crackers Explained</a></h3>
                    <p>Understanding eco-friendly fireworks and how they help reduce emissions.</p>
                </div>
                <div class="blog-card">
                    <h3><a href="/blog/fireworks-safety-checklist.html">Fireworks Safety Checklist</a></h3>
                    <p>Ensure your family stays safe this festival season with these vital tips.</p>
                </div>
            </div>
        </section>

        <section class="faq-section mt-5">
            <h2>Frequently Asked Questions</h2>
            {faqs_html}
        </section>
        
        <section class="internal-links mt-5" style="border-top: 1px solid #e5e7eb; padding-top: 20px;">
            <h4>Quick Links</h4>
            <a href="/index.html">Home</a>
            <a href="/crackers-buying-guide.html">Buying Guide</a>
            <a href="/safety-guide.html">Safety Guide</a>
            <a href="/festival-guide.html">Festival Guide</a>
            <a href="/blog/index.html">Blog</a>
        </section>
    </main>

    {SHARED_FOOTER}
    
    <script src="/js/main.js"></script>
</body>
</html>
"""
    file_path = os.path.join(CAT_DIR, f"{cat['slug']}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {file_path}")

for cat in categories:
    generate_html(cat)

print("All category pages generated successfully.")
