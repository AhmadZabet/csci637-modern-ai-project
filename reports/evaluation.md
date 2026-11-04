# Adapted evaluation set, version 2

4 November 2026 | OpenAI Codex

All 16 issues recorded in the previous audit have documented editorial resolutions. This is a project-adapted SciQ set, not an unchanged benchmark. It contains 100 items with the same four-subject distribution.

Only item 2 retains an unchanged human-confirmed version. Item 1 was previously human-confirmed but its revised wording is AI-reviewed. All other items have AI-review provenance. No new human approval is inferred.

Original source questions, alternatives and full supporting passages remain available. Three items use exact evidence excerpts to avoid defective or irrelevant surrounding sentences; this does not repair the original retrieval corpus. When reporting evidence-based scores, specify which evidence field is supplied.

Source: https://huggingface.co/datasets/allenai/sciq | Welbl, Liu and Gardner (2017) | CC BY-NC 3.0. Changes are recorded in data/evaluation/evaluation_adaptations_v2.json.

## Revised items

### 1. sciq_test_00566_adapted_v2
Question omits maximum depth; existing review note supplies a qualification absent from the question.

According to the passage, what maximum depth in meters can the photic zone reach?

### 8. sciq_test_00782_adapted_v2
Tectonic movement is broader than transform plate boundary and fits the loose wording.

What type of plate boundary forms where two plates slide past each other?

### 10. sciq_test_00164_adapted_v2
Passage describes skeletal muscle but does not establish exclusivity against the heart-muscle option.

According to the passage, myofibrils run the entire length of which type of muscle fiber?

### 14. sciq_test_00036_adapted_v2
Amps and amperes are synonymous alternatives.

In which unit is heat energy measured?

### 16. sciq_test_00899_adapted_v2
The ideal-gas qualification is supplied only in the review note.

Which theory, in its ideal-gas model, neglects intermolecular interactions between gas particles?

### 31. sciq_test_00599_adapted_v2
Evaporation is a component of the process; intended named plant process should be explicit.

What is the specific name for water loss as vapor from plants through leaf stomata?

### 39. sciq_test_00353_adapted_v2
The passage says slow neuron; this error could propagate to explanations.

According to the passage, which nuclear process produces smaller nuclei, additional neutrons, and heat?

### 50. sciq_test_00863_adapted_v2
The passage describes higher pH as a stronger base without controlling concentration; the question also leaves conditions implicit.

In the introductory aqueous-solution context of the passage, a pH above 7 indicates which option?

### 57. sciq_test_00417_adapted_v2
Energy and products can both satisfy the broad phrase what else.

What name is given to the substances formed by a chemical reaction?

### 58. sciq_test_00110_adapted_v2
The passage explicitly includes ecology within Biology, another choice.

Which specialized branch of biology studies interactions among organisms and their environment?

### 60. sciq_test_00128_adapted_v2
Question universally equates absence of a nucleus with the prokaryotic category; review note already records exceptions.

In the prokaryotic/eukaryotic distinction described in the passage, which cell category lacks a nucleus?

### 73. sciq_test_00177_adapted_v2
Subtraction requires opposing collinear forces; the question and one-sentence evidence omit this.

An object has an applied force and an opposing frictional force along one line, with all other forces balanced. What is the applied force minus friction?

### 84. sciq_test_00465_adapted_v2
Requiring attention to what is underspecified; passage also uses total internal refraction after describing reflection.

Which property of the fiber and its surrounding coating must be appropriately chosen to permit total internal reflection?

### 88. sciq_test_00698_adapted_v2
Resistance comparison needs controlled length and material; question omits both.

Two wires have the same material, length and temperature. Which property is greater for the narrower wire?

### 96. sciq_test_00414_adapted_v2
Astronomical observing band and reflector design/location are different dimensions; radio and reflecting/space telescopes need not be exclusive.

Which telescope category is defined by detecting radio waves?

### 97. sciq_test_00189_adapted_v2
Light months is also a distance unit; intended conventional unit is not uniquely established by the broad question.

What distance unit is defined as the distance light travels in one year?

## Complete adapted set

### 1. sciq_test_00566_adapted_v2 | Earth and Space Science
According to the passage, what maximum depth in meters can the photic zone reach?

- A: 100
- B: 200
- C: 900
- D: 400

Answer: B - 200
Review: ai_reviewed_adaptation
Evidence:
The photic zone extends to a maximum depth of 200 meters (656 feet) below the surface of the water. This is where enough sunlight penetrates for photosynthesis to occur. Algae and other photosynthetic organisms can make food and support food webs.

### 2. sciq_test_00234 | Physics
A solenoid wrapped around a bar of iron or other ferromagnetic material forms what?

- A: electromagnet
- B: impoundment
- C: compass
- D: compress

Answer: A - electromagnet
Review: human_confirmed
Evidence:
Solenoids are the basis of electromagnets. An electromagnet is a solenoid wrapped around a bar of iron or other ferromagnetic material (see Figure below ). The electromagnetic field of the solenoid magnetizes the iron bar by aligning its magnetic domains. The combined magnetic force of the magnetized iron bar and the wire coil makes an electromagnet very strong. In fact, electromagnets are the strongest magnets made. Some of them are strong enough to lift a train. The maglev train described earlier, in the lesson "Electricity and Magnetism," contains permanent magnets. Strong electromagnets in the track repel the train magnets, causing the train to levitate above the track.

### 3. sciq_test_00309 | Biology
The amniotic egg is a shared ancestral character for which clade?

- A: xerophyte
- B: avian
- C: amniota
- D: trichina

Answer: C - amniota
Review: ai_reviewed
Evidence:
What is the largest clade in this diagram? Shared Characteristics Organisms evolve from common ancestors and then diversify. Scientists use the phrase “descent with modification” because even though related organisms have many of the same characteristics and genetic codes, changes occur. This pattern repeats over and over as one goes through the phylogenetic tree of life: 1. A change in the genetic makeup of an organism leads to a new trait which becomes prevalent in the group. Many organisms descend from this point and have this trait. New variations continue to arise: some are adaptive and persist, leading to new traits. With new traits, a new branch point is determined (go back to step 1 and repeat). If a characteristic is found in the ancestor of a group, it is considered a shared ancestral character because all of the organisms in the taxon or clade have that trait. The vertebrate in Figure 20.10 is a shared ancestral character. Now consider the amniotic egg characteristic in the same figure. Only some of the organisms in Figure 20.10 have this trait, and to those that do, it is called a shared derived character because this trait derived at some point but does not include all of the ancestors in the tree. The tricky aspect to shared ancestral and shared derived characters is the fact that these terms are relative. The same trait can be considered one or the other depending on the particular diagram being used. Returning to Figure 20.10, note that the amniotic egg is a shared ancestral character for the Amniota clade, while having hair is a shared derived character for some organisms in this group. These terms help scientists distinguish between clades in the building of phylogenetic trees.

### 4. sciq_test_00171 | Biology
What is the protein in red blood cells which transports oxygen around the body?

- A: hematocrit
- B: plasma
- C: hydrogen
- D: hemoglobin

Answer: D - hemoglobin
Review: ai_reviewed
Evidence:
What do you see when you look at this picture? Is it just a mass of tangled ribbons? Look closely. It’s actually a complex pattern of three-dimensional shapes. It represents the structure of a common chemical found inside living cells. The chemical is a protein called hemoglobin. It is the protein in red blood cells which transports oxygen around the body.

### 5. sciq_test_00337 | Chemistry
Salicylic acid is used in the synthesis of acetylsalicylic acid, or more commonly called?

- A: smelling salts
- B: aspirin
- C: Tylenol
- D: antacid

Answer: B - aspirin
Review: ai_reviewed
Evidence:
Salicylic acid is used in the synthesis of acetylsalicylic acid, or aspirin. One gram dissolves in 460 mL of water to create a saturated solution with a pH of 2.40.

### 6. sciq_test_00521 | Chemistry
What term means the set of processes by which metals are extracted from their ores and converted to more useful forms?

- A: metamorphisis
- B: introversion
- C: metallurgy
- D: ceramics

Answer: C - metallurgy
Review: ai_reviewed
Evidence:
Very few of the transition metals are found in nature as free metals. Consequently, almost all metallic elements must be isolated from metal oxide or metal sulfide ores. Metallurgy is the set of processes by which metals are extracted from their ores and converted to more useful forms. Metallurgy consists of three general steps: (1) mining the ore, (2) separating and concentrating the metal or the metal-containing compound, and (3) reducing the ore to the metal. Additional processes are sometimes required to improve the mechanical properties of the metal or increase its purity. Many ores contain relatively low concentrations of the desired metal; for example, copper ores that contain even 1% Cu by mass are considered commercially useful. After an ore has been mined, the first step in processing is usually to crush it because the rate of chemical reactions increases dramatically with increased surface area. Next, one of three general strategies is used to separate and concentrate the compound(s) of interest: settling and flotation, which are based on differences in density between the desired compound and impurities; pyrometallurgy, which uses chemical reduction at high temperatures; and hydrometallurgy, which employs chemical or electrochemical reduction of an aqueous solution of the metal. Other methods that take advantage of unusual physical or chemical properties of a particular compound may also be used. For example, crystals of magnetite (Fe3O4) are tiny but rather powerful magnets; in fact, magnetite (also known as lodestone) was used to make the first compasses in China during the first century BC. If a crushed ore that contains magnetite is passed through a powerful magnet, the Fe3O4 particles are attracted to the poles of the magnet, allowing them to be easily separated from other minerals.

### 7. sciq_test_00096 | Chemistry
Water can be broken down into hydrogen and oxygen gases by the addition of what?

- A: energy
- B: motion
- C: mineral
- D: demand

Answer: A - energy
Review: ai_reviewed
Evidence:
Chemistry in Everyday Life Decomposition of Water / Production of Hydrogen Water consists of the elements hydrogen and oxygen combined in a 2 to 1 ratio. Water can be broken down into hydrogen and oxygen gases by the addition of energy. One way to do this is with a battery or power supply, as shown in (Figure 1.15).

### 8. sciq_test_00782_adapted_v2 | Earth and Space Science
What type of plate boundary forms where two plates slide past each other?

- A: convergent plate boundary
- B: transform plate boundary
- C: divergent plate boundary
- D: subduction boundary

Answer: B - transform plate boundary
Review: ai_reviewed_adaptation
Evidence:
Two plates may slide past each other in opposite directions. This is called a transform plate boundary . The plates meet at a transform fault . As you might imagine, plates do not slide past each other easily. These plate boundaries experience massive earthquakes. The world’s best known transform fault is the San Andreas Fault in California ( Figure below ). At this fault, the Pacific and North American plates grind past each other. Transform plate boundaries are common as offsets along mid-ocean ridges. They are very small compared to transform faults on land.

### 9. sciq_test_00077 | Physics
What is required to move or change matter from one state to another?

- A: energy
- B: evolution
- C: food
- D: gravity

Answer: A - energy
Review: ai_reviewed
Evidence:
Energy provides the ability to move or change matter from one state to another (for example, from solid to liquid). Every living thing needs energy to live and grow. Your body gets its energy from food, but that is only a small part of the energy you use every day. Cooking your food takes energy, and so does keeping it cold in the refrigerator or the freezer. The same is true for heating or cooling your home. Whether you are turning on a light in the kitchen or riding in a car to school, you are using energy. Billions of people all around the world use energy, so there is a huge demand for resources to provide all of this energy. Why do we need so much energy? The main reason is that almost everything that happens on Earth involves energy.

### 10. sciq_test_00164_adapted_v2 | Biology
According to the passage, myofibrils run the entire length of which type of muscle fiber?

- A: collagen fibers
- B: elastic fibers
- C: nerve fibers
- D: skeletal muscle fibers

Answer: D - skeletal muscle fibers
Review: ai_reviewed_adaptation
Evidence:
Skeletal Muscle Fiber Structure and Function Each skeletal muscle fiber is a skeletal muscle cell. Within each muscle fiber are myofibrils, long cylindrical structures that lie parallel to the muscle fiber. Myofibrils run the entire length of the muscle fiber. They attach to the plasma membrane, called the sarcolemma, at their ends, so that as myofibrils shorten, the entire muscle cell contracts (Figure 16.18).

### 11. sciq_test_00785 | Earth and Space Science
What is the eighth planet from our sun?

- A: uranus
- B: earth
- C: neptune
- D: mars

Answer: C - neptune
Review: ai_reviewed
Evidence:
Neptune is shown in Figure below . It is the eighth planet from the Sun. Neptune is so far away you need a telescope to see it from Earth. Neptune is the most distant planet in our solar system. It is nearly 4.5 billion kilometers (2.8 billion miles) from the Sun. One orbit around the Sun takes Neptune 165 Earth years.

### 12. sciq_test_00833 | Biology
All types of cells are enclosed by what?

- A: substrate
- B: membrane
- C: cell wall
- D: stoma

Answer: B - membrane
Review: ai_reviewed
Evidence:
Regardless of the type of organism, all living cells share certain basic structures. For example, all cells are enclosed by a membrane. The cell membrane separates the cell from its environment. It also controls what enters or leaves the cell.

### 13. sciq_test_00175 | Biology
At a synapse, what objects are released to carry a nerve impulse from one neuron to the next?

- A: microorganisms
- B: receptors
- C: viruses
- D: neurotransmitters

Answer: D - neurotransmitters
Review: ai_reviewed
Evidence:
Laura Guerin. At a synapse, neurotransmitters are released to carry a nerve impulse from one neuron to the next . CC BY-NC 3.0.

### 14. sciq_test_00036_adapted_v2 | Chemistry
In which unit is heat energy measured?

- A: amperes
- B: meters
- C: seconds
- D: joules

Answer: D - joules
Review: ai_reviewed_adaptation
Evidence:
Chemical reactions involve a transfer of heat energy. Measured in joules.

### 15. sciq_test_00259 | Biology
What process, which is in many ways the opposite of photosynthesis, shows the interdependence of producers and consumers?

- A: osmosis
- B: cellular respiration
- C: decomposition
- D: primarily respiration

Answer: B - cellular respiration
Review: ai_reviewed
Evidence:
Cellular respiration, in many ways the opposite of photosynthesis, shows the interdependence of producers and consumers. Combined, the two equations demonstrate how energy flows and the carbon and oxygen cycle between organisms and environment.

### 16. sciq_test_00899_adapted_v2 | Physics
Which theory, in its ideal-gas model, neglects intermolecular interactions between gas particles?

- A: Avoidance theory
- B: viscosity theory
- C: vortex theory
- D: kinetic theory

Answer: D - kinetic theory
Review: ai_reviewed_adaptation
Evidence:
The kinetic theory also states that there is no interaction between individual gas particles. Although we know that there are, in fact, intermolecular interactions in real gases, the kinetic theory assumes that gas particles are so far apart that the individual particles don’t “feel” each other. Thus, we can treat gas particles as tiny bits of matter whose identity isn’t important to certain physical properties.

### 17. sciq_test_00548 | Physics
What term is used to describe is the spontaneous emission of particles and radiation from atomic nuclei?

- A: intensity
- B: microscopic
- C: radioactivity
- D: vibration

Answer: C - radioactivity
Review: ai_reviewed
Evidence:
Radioactivity is the spontaneous emission of particles and radiation from atomic nuclei.

### 18. sciq_test_00210 | Earth and Space Science
What type of eclipse happens when a full moon moves through earth's shadow?

- A: solar
- B: lunar
- C: cycle
- D: planetary

Answer: B - lunar
Review: ai_reviewed
Evidence:
Sometimes a full moon moves through Earth's shadow. This is a lunar eclipse ( Figure below ). During a total lunar eclipse, the Moon travels completely in Earth’s umbra. During a partial lunar eclipse, only a portion of the Moon enters Earth’s umbra. When the Moon passes through Earth’s penumbra, it is a penumbral eclipse. Since Earth’s shadow is large, a lunar eclipse lasts for hours. Anyone with a view of the Moon can see a lunar eclipse.

### 19. sciq_test_00798 | Chemistry
Free fatty acids are carboxylic acids that contain long chains of what?

- A: vapors
- B: particles
- C: lipds
- D: hydrocarbons

Answer: D - hydrocarbons
Review: ai_reviewed
Evidence:
In the Figure below , we see the structures of some common classes of lipids. Free fatty acids are carboxylic acids that contain long hydrocarbon chains. Saturated fatty acids are alkanes with a single carboxylic acid, whereas unsaturated fatty acids contain one or more C-C double bonds. Fatty acids often form esters with one of the alcohol functional groups on glycerol , a three carbon chain in which each carbon is bonded to one OH group. Triglycerides are common structures, in which all three of these OH groups are esterified with a fatty acid. The three fatty acids in a triglyceride may be the same or different. Another common structure is a phospholipid, in which two of the alcohols in glycerol form esters with fatty acids, and the third is connected to a very polar phosphorus-containing group.

### 20. sciq_test_00584 | Biology
How do multicellular organisms grow in size?

- A: increase size and number of genes
- B: increase number of limbs
- C: reduce size and number of cells
- D: increase size and number of cells

Answer: D - increase size and number of cells
Review: ai_reviewed
Evidence:
Like plants, all living things have the capacity for growth. The ducklings in Figure below have a lot of growing to do to catch up in size to their mother. Multicellular organisms like ducks grow by increasing the size and number of their cells. Single-celled organisms just grow in size.

### 21. sciq_test_00297 | Physics
What can we learn about a wave by finding the product of the wavelength and frequency?

- A: speed
- B: volume
- C: decibels
- D: type

Answer: A - speed
Review: ai_reviewed
Evidence:
The speed of a wave is a product of its wavelength and frequency. Because all electromagnetic waves travel at the same speed through space, a wave with a shorter wavelength must have a higher frequency, and vice versa. This relationship is represented by the equation:.

### 22. sciq_test_00268 | Biology
Traits may also be controlled by multiple alleles or multiple what?

- A: genes
- B: eggs
- C: chromosomes
- D: lesions

Answer: A - genes
Review: ai_reviewed
Evidence:
Inheritance is more complex for traits in which there is codominance or incomplete dominance. Traits may also be controlled by multiple alleles or multiple genes. Many traits are influenced by the environment as well.

### 23. sciq_test_00510 | Earth and Space Science
What is made of molecules of many different gases, and is something we usually can’t see, taste, or smell; we can only feel it when it moves?

- A: air
- B: light
- C: sound
- D: water

Answer: A - air
Review: ai_reviewed
Evidence:
Air is easy to forget about. We usually can’t see it, taste it, or smell it. We can only feel it when it moves. But air is actually made of molecules of many different gases. It also contains tiny particles of solid matter.

### 24. sciq_test_00448 | Biology
What hormone secreted by the pineal gland controls sleep-wake cycles and several other processes?

- A: testosterone
- B: melatonin
- C: t3
- D: estrogen

Answer: B - melatonin
Review: ai_reviewed
Evidence:
The pineal gland is a tiny gland located at the base of the brain. It secretes the hormone melatonin . This hormone controls sleep-wake cycles and several other processes.

### 25. sciq_test_00920 | Earth and Space Science
In the grand canyon, the same rock layers are visible on opposite sides of the canyon and were deposited simultaneously, which is an example of what?

- A: directly continuity
- B: width continuity
- C: bilateral continuity
- D: lateral continuity

Answer: D - lateral continuity
Review: ai_reviewed
Evidence:
Look at the Grand Canyon in Figure below . It’s a good example of lateral continuity. You can clearly see the same rock layers on opposite sides of the canyon. The matching rock layers were deposited at the same time, so they are the same age.

### 26. sciq_test_00968 | Chemistry
The first two electrons in lithium fill the 1s orbital and have the same sets of four what as the two electrons in helium?

- A: quantum numbers
- B: decay numbers
- C: kinetic numbers
- D: gravity numbers

Answer: A - quantum numbers
Review: ai_reviewed
Evidence:
The n = 1 shell is completely filled in a helium atom. The next atom is the alkali metal lithium with an atomic number of 3. The first two electrons in lithium fill the 1s orbital and have the same sets of four quantum numbers as the two electrons in helium. The remaining electron must occupy the orbital of next lowest energy, the 2s orbital (Figure 6.27 or Figure 6.28). Thus, the electron configuration and orbital diagram of lithium are:.

### 27. sciq_test_00421 | Biology
Paramecium possess tiny hair-like cilia that help them do what?

- A: look
- B: breed
- C: move
- D: fight

Answer: C - move
Review: ai_reviewed
Evidence:
Some protists, like these Paramecium , act much like animals. Notice the tiny hair-like cilia that help them move. The food vacuoles, where they digest their prey, are colored in orange.

### 28. sciq_test_00093 | Biology
Skeletal muscles are attached to the skeleton by tough connective tissues called what?

- A: cords
- B: fibers
- C: tendons
- D: veins

Answer: C - tendons
Review: ai_reviewed
Evidence:
Skeletal muscles are attached to the skeleton by tough connective tissues called tendons (see Figure above ). Many skeletal muscles are attached to the ends of bones that meet at a joint . The muscles span the joint and connect the bones. When the muscles contract, they pull on the bones, causing them to move.

### 29. sciq_test_00211 | Chemistry
Dynamite is an example of what type of potential energy?

- A: carbon
- B: mineral
- C: thermal
- D: chemical

Answer: D - chemical
Review: ai_reviewed
Evidence:
Dynamite is another example of chemical potential energy. The major component of dynamite is nitroglycerin, a very unstable material. By mixing it with diatomaceous earth, the stability is increased and it is less likely to explode if it receives a physical shock. When ignited, the nitroglycerin explodes rapidly, releasing large amounts of nitrogen and other gases along with a massive amount of heat.

### 30. sciq_test_00089 | Biology
What is the diffusion of water through a semipermeable membrane down its concentration gradient

- A: nutrients
- B: mirrors
- C: osmosis
- D: Permable

Answer: C - osmosis
Review: ai_reviewed
Evidence:
Figure 3.7 Osmosis Osmosis is the diffusion of water through a semipermeable membrane down its concentration gradient. If a membrane is permeable to water, though not to a solute, water will equalize its own concentration by diffusing to the side of lower water concentration (and thus the side of higher solute concentration). In the beaker on the left, the solution on the right side of the membrane is hypertonic.

### 31. sciq_test_00599_adapted_v2 | Biology
What is the specific name for water loss as vapor from plants through leaf stomata?

- A: germination
- B: pollination
- C: transpiration
- D: fertilization

Answer: C - transpiration
Review: ai_reviewed_adaptation
Evidence:
Transpiration takes place when plants release water vapor through pores in their leaves called stomata.

### 32. sciq_test_00321 | Biology
Ecological succession refers to the change in the numbers and types of species that live in what groups?

- A: movements
- B: colonies
- C: biomes
- D: communities

Answer: D - communities
Review: ai_reviewed
Evidence:
Communities are not usually static. The numbers and types of species that live in them generally change over time. This is called ecological succession . Important cases of succession are primary and secondary succession.

### 33. sciq_test_00324 | Chemistry
The number of what subatomic particles determines an element’s atomic number and is used to distinguish one element from another?

- A: quarks
- B: protons
- C: electrons
- D: neutrons

Answer: B - protons
Review: ai_reviewed
Evidence:
Atomic Number and Mass Atoms of each element contain a characteristic number of protons and electrons. The number of protons determines an element’s atomic number and is used to distinguish one element from another. The number of neutrons is variable, resulting in isotopes, which are different forms of the same atom that vary only in the number of neutrons they possess. Together, the number of protons and the number of neutrons determine an element’s mass number, as illustrated in Figure 2.3. Note that the small contribution of mass from electrons is disregarded in calculating the mass number. This approximation of mass can be used to easily calculate how many neutrons an element has by simply subtracting the number of protons from the mass number. Since an element’s isotopes will have slightly different mass numbers, scientists also determine the atomic mass, which is the calculated mean of the mass number for its naturally occurring isotopes. Often, the resulting number contains a fraction. For example, the atomic mass of chlorine (Cl) is 35.45 because chlorine is composed of several isotopes, some (the majority) with atomic mass 35 (17 protons and 18 neutrons) and some with atomic mass 37 (17 protons and 20 neutrons).

### 34. sciq_test_00888 | Physics
What term describes the distance between two corresponding points on adjacent waves?

- A: variation
- B: wavelength
- C: frequency
- D: threshold

Answer: B - wavelength
Review: ai_reviewed
Evidence:
Another important measure of wave size is wavelength. Wavelength is the distance between two corresponding points on adjacent waves (see Figure above ). Wavelength can be measured as the distance between two adjacent crests of a transverse wave or two adjacent compressions of a longitudinal wave. It is usually measured in meters. Wavelength is related to the energy of a wave. Short-wavelength waves have more energy than long-wavelength waves of the same amplitude. You can see examples of waves with shorter and longer wavelengths in Figure below .

### 35. sciq_test_00131 | Biology
What disease characterized by the extreme swelling of the limbs is caused by infection with a type of roundworm?

- A: elephantiasis
- B: fibrosis
- C: gigantism
- D: pulmonary edema

Answer: A - elephantiasis
Review: ai_reviewed
Evidence:
Roundworms can be free-living organisms, but they are probably best known for their role as significant plant and animal parasites. Most Nematodes are parasitic, with over 16,000 parasitic species described. Heartworms, which cause serious disease in dogs while living in the heart and blood vessels, are a type of roundworm. Roundworms can also cause disease in humans. Elephantiasis, a disease characterized by the extreme swelling of the limbs ( Figure below ), is caused by infection with a type of roundworm.

### 36. sciq_test_00452 | Biology
What is the female reproductive structure of a flower?

- A: the flower
- B: the stamen
- C: the seed
- D: the pistil

Answer: D - the pistil
Review: ai_reviewed
Evidence:
The pistil is the female reproductive structure of a flower. It consists of a stigma, style , and ovary . The stigma is raised and sticky to help it catch pollen. The style supports the stigma and connects it to the ovary, which contains the egg. Petals attract pollinators to the flower. Petals are often brightly colored so pollinators will notice them.

### 37. sciq_test_00916 | Biology
Under what type of conditions can populations grow exponentially?

- A: pleasant
- B: ideal
- C: lush
- D: useful

Answer: B - ideal
Review: ai_reviewed
Evidence:
Under ideal conditions, populations can grow exponentially. The growth rate increases as the population gets larger. Most populations do not live under ideal conditions and grow logistically instead. Density-dependent factors slow population growth as population size nears the carrying capacity.

### 38. sciq_test_00447 | Chemistry
Matter undergoing chemical reactions and physical changes can release or absorb heat. a change that releases heat is called what?

- A: biochemical process
- B: exothermic process
- C: oxidized process
- D: magnetic process

Answer: B - exothermic process
Review: ai_reviewed
Evidence:
Matter undergoing chemical reactions and physical changes can release or absorb heat. A change that releases heat is called an exothermic process. For example, the combustion reaction that occurs when using an oxyacetylene torch is an exothermic process—this process also releases energy in the form of light as evidenced by the torch’s flame (Figure 5.7). A reaction or change that absorbs heat is an endothermic process. A cold pack used to treat muscle strains provides an example of an endothermic process. When the substances in the cold pack (water and a salt like ammonium nitrate) are brought together, the resulting process absorbs heat, leading to the sensation of cold.

### 39. sciq_test_00353_adapted_v2 | Physics
According to the passage, which nuclear process produces smaller nuclei, additional neutrons, and heat?

- A: fusion
- B: diffusion
- C: Reaction
- D: fission

Answer: D - fission
Review: ai_reviewed_adaptation
Evidence:
The products of a fission reaction are two smaller isotopes, more neutrons, and heat energy.

### 40. sciq_test_00115 | Biology
What disease occurs when the cell cycle is no longer regulated?

- A: schizophrenia
- B: allergy
- C: malnutrition
- D: cancer

Answer: D - cancer
Review: ai_reviewed
Evidence:
Cancer is a disease that occurs when the cell cycle is no longer regulated. Cancer cells grow rapidly and may form a mass of abnormal cells called a tumor.

### 41. sciq_test_00169 | Biology
What broad animal group is thought to have evolved from theropod dinosaurs around 150 million years ago?

- A: insects
- B: birds
- C: mammals
- D: reptiles

Answer: B - birds
Review: ai_reviewed
Evidence:
Birds are thought to have evolved from theropod dinosaurs around 150 million years ago. Their ancestor may have been similar to the extinct theropod Deinonychus, whose fossils convinced most scientists that birds evolved from dinosaurs. Scientist still don’t know how or why wings and flight evolved, but they continue to search for answers.

### 42. sciq_test_00258 | Earth and Space Science
When a stream or river slows down, it starts dropping its what?

- A: sediments
- B: pollutants
- C: fragments
- D: organisms

Answer: A - sediments
Review: ai_reviewed
Evidence:
When a stream or river slows down, it starts dropping its sediments. Larger sediments are dropped in steep areas, but smaller sediments can still be carried. Smaller sediments are dropped as the slope becomes less steep.

### 43. sciq_test_00319 | Chemistry
A thermite reaction is thermodynamically spontaneous, and because it is associated with a significant release of heat, it is regarded as what?

- A: endotropic
- B: biochemical
- C: endothermic
- D: exothermic

Answer: D - exothermic
Review: ai_reviewed
Evidence:
Thermodynamic spontaneity. The highly exothermic and dramatic thermite reaction is thermodynamically spontaneous. Reactants of aluminum and a metal oxide, usually iron, which are stable at room temperature, are ignited either in the presence of heat or by the reaction of potassium permanganate and glycerin. The resulting products are aluminum oxide, free and molten elemental metal, and a great deal of heat, which makes this an excellent method for on-site welding. Because this reaction has its own oxygen supply, it can be used for underwater welding as well.

### 44. sciq_test_00373 | Earth and Space Science
Some types of minerals form balls called what?

- A: nodules
- B: fistulas
- C: microbes
- D: cancers

Answer: A - nodules
Review: ai_reviewed
Evidence:
Some types of minerals form balls called nodules. Nodules may be tiny or as big as basketballs. They contain manganese, iron, copper, and other useful minerals. As many as 500 billion tons of nodules lie on the ocean floor! However, mining them would be very costly and could be harmful to the ocean environment.

### 45. sciq_test_00707 | Physics
What type of mirror is shaped like the outside of a bowl?

- A: convex
- B: vertex
- C: slope
- D: concave

Answer: A - convex
Review: ai_reviewed
Evidence:
The other type of curved mirror, a convex mirror, is shaped like the outside of a bowl. Because of its shape, it can gather and reflect light from a wide area. As you can see in the Figure below , a convex mirror forms only virtual images that are right-side up and smaller than the actual object. You can see how a convex mirror forms an image in the animation at this URL: http://physics. slss. ie/resources/convex%20mirror. swf.

### 46. sciq_test_00370 | Biology
There are 20 different common amino acids needed to make what organic compound?

- A: proteins
- B: nutron
- C: lipids
- D: cells

Answer: A - proteins
Review: ai_reviewed
Evidence:
Proteins are organic compounds that contain carbon, hydrogen, oxygen, nitrogen, and, in some cases, sulfur. These compounds may many essential functions within the cell (see below). Proteins are made of smaller units called amino acids . There are 20 different common amino acids needed to make proteins. All amino acids have the same basic structure, which is shown in Figure below . Only the side chain (labeled R in the figure) differs from one amino acid to another. These side chains can vary in size from just one hydrogen atom in glycine to a large heterocyclic group in tryptophan. The variable side chain gives each amino acid unique properties. The side chains can also characterize the amino acid as (1) nonpolar or hydrophobic, (2) neutral (uncharged) but polar, (3) acidic, with a net negative charge, and (4) basic, with a net positive charge at neutral pH.

### 47. sciq_test_00264 | Biology
The chemical and/or physical agents that cause mutations are called what?

- A: dioxins
- B: genes
- C: mutagens
- D: organelles

Answer: C - mutagens
Review: ai_reviewed
Evidence:
mutation. The chemical and/or physical agents that cause mutations are called mutagens. Diseases that occur due to mutations in critical DNA sequences are referred to as genetic diseases. Viruses are infectious agents composed of a tightly packed central core of nucleic acids enclosed by a protective shell of proteins. Viruses contain either DNA or RNA as their genetic material but not both. Some RNA viruses, calledretroviruses, synthesize DNA in the host cell from their RNA genome. The human immunodeficiency virus (HIV) causes acquired immunodeficiency syndrome (AIDS).

### 48. sciq_test_00873 | Biology
Temperature and precipitation determine the types of what that can grow in an area, in turn affecting the animals that live there?

- A: building
- B: birds
- C: roots
- D: plants

Answer: D - plants
Review: ai_reviewed
Evidence:
Temperature and precipitation determine what types of plants can grow in an area. Animals and other living things depend on plants. So each climate is associated with certain types of living things. A major type of climate and its living things make up a biome . As you read about the major climate types below, find them on the map above ( Figure above ).

### 49. sciq_test_00144 | Biology
What opens two strands of dna?

- A: adenylate
- B: chromosome
- C: helicase
- D: replication

Answer: C - helicase
Review: ai_reviewed
Evidence:
DNA replication. The two DNA strands are opened by helicase. The strands are held open by a single strand of binding proteins, preventing premature reannealing. Topoisomerase solves the problem caused by tension generated by winding/unwinding of DNA. This enzyme wraps around DNA and makes a cut permitting the helix to spin and relax. Once DNA is relaxed, topoisomerase reconnects broken strands. DNA primase synthesizes a short RNA primer which initiates the Okazaki fragment. Okazaki fragments are attached by DNA ligase.

### 50. sciq_test_00863_adapted_v2 | Chemistry
In the introductory aqueous-solution context of the passage, a pH above 7 indicates which option?

- A: base
- B: volatile
- C: neutral
- D: acidic

Answer: A - base
Review: ai_reviewed_adaptation
Evidence:
A pH value greater than 7 indicates a base

### 51. sciq_test_00019 | Earth and Space Science
What term means the amount of water vapor in the air?

- A: humidity
- B: ambient
- C: pressure
- D: temperature

Answer: A - humidity
Review: ai_reviewed
Evidence:
Humidity is the amount of water vapor in the air. High humidity increases the chances of clouds and precipitation.

### 52. sciq_test_00505 | Biology
What are the small molecules or proteins produced by bacteria that regulate gene expression?

- A: protazoas
- B: fluxes
- C: sporozoans
- D: autoinducers

Answer: D - autoinducers
Review: ai_reviewed
Evidence:
Figure 9.17 Autoinducers are small molecules or proteins produced by bacteria that regulate gene expression.

### 53. sciq_test_00638 | Chemistry
The basic voltaic cell variations are the dry cell and the what?

- A: lead storage battery
- B: lead flood battery
- C: lead electricity battery
- D: positive terminal

Answer: A - lead storage battery
Review: ai_reviewed
Evidence:
Two variations on the basic voltaic cell are the dry cell and the lead storage battery.

### 54. sciq_test_00585 | Chemistry
What symbol is used to indicate directionality in chemical reactions?

- A: triangle
- B: circle
- C: arrow
- D: line

Answer: C - arrow
Review: ai_reviewed
Evidence:
The arrow (→) shows the direction in which the reaction occurs. In many reactions, the reaction also occurs in the opposite direction. This is represented with another arrow pointing in the opposite direction (←).

### 55. sciq_test_00148 | Biology
What are classified by climatic factors and types of primary producers?

- A: old biomes
- B: equivalent biomes
- C: fossil biomes
- D: terrestrial biomes

Answer: D - terrestrial biomes
Review: ai_reviewed
Evidence:
Terrestrial biomes are classified by climatic factors and types of primary producers. The world map in Figure below shows where 13 major terrestrial biomes are found.

### 56. sciq_test_00811 | Earth and Space Science
Which part of the atmosphere do greenhouse gasses trap heat in?

- A: thermosphere
- B: troposphere
- C: lithosphere
- D: stratosphere

Answer: B - troposphere
Review: ai_reviewed
Evidence:
Greenhouse gases trap heat in the troposphere. Some greenhouse gases can trap more heat than others.

### 57. sciq_test_00417_adapted_v2 | Chemistry
What name is given to the substances formed by a chemical reaction?

- A: solvents
- B: reactants
- C: catalysts
- D: products

Answer: D - products
Review: ai_reviewed_adaptation
Evidence:
All chemical reactions involve both reactants and products. Reactants are substances that start a chemical reaction, and products are substances that are produced in the reaction.

### 58. sciq_test_00110_adapted_v2 | Biology
Which specialized branch of biology studies interactions among organisms and their environment?

- A: genetics
- B: cell biology
- C: ecology
- D: biochemistry

Answer: C - ecology
Review: ai_reviewed_adaptation
Evidence:
Most biological sciences are specialized areas of study. Biology includes biochemistry, cell biology, microbiology, immunology, genetics, physiology, zoology, ecology, evolutionary biology, and botany. Biochemistry is the study of the chemicals that make up life. Cell biology is the study of life at the level of the cell. Microbiology is the study of microscopic organisms. Immunology is the study of an organism's resistance to disease. Genetics is the study of how organisms pass traits to their offspring. The study of how the human body works is called physiology. Zoology is the study of animals. The study of how organisms interact with their environment and each other is called ecology. Evolutionary biology is the study of how populations and species change over time. Botany is the study of plants. The four unifying principles are important foundations for each and every field of biology. Applied fields of biology such as medicine and genetic research involve many specialized areas of study.

### 59. sciq_test_00076 | Biology
The lens and other parts of the eye work together to focus a real image on what eye structure?

- A: cornea
- B: iris
- C: pupil
- D: retina

Answer: D - retina
Review: ai_reviewed
Evidence:
As just described, the eyes collect and focus visible light. The lens and other structures of the eye work together to focus a real image on the retina. The image is upside-down and reduced in size, as you can see in Figure below . The image reaches the brain as electrical signals that travel through the optic nerve. The brain interprets the signals as shape, color, and brightness. It also interprets the image as though it were right-side up. The brain does this automatically, so what we see is always right-side up. The brain also “tells” us what we are seeing.

### 60. sciq_test_00128_adapted_v2 | Biology
In the prokaryotic/eukaryotic distinction described in the passage, which cell category lacks a nucleus?

- A: Monocyte Cells
- B: prokaryotic cells
- C: heterogeneous cells
- D: crustal cells

Answer: B - prokaryotic cells
Review: ai_reviewed_adaptation
Evidence:
Prokaryotic cells are cells without a nucleus. They are found in single-celled organisms. Eukaryotic cells are cells with a nucleus and other organelles. They are found mainly in multicellular organisms.

### 61. sciq_test_00611 | Biology
The cell membrane consists of two layers of what?

- A: phospholipids
- B: epidermis
- C: filaments
- D: chlorophyll

Answer: A - phospholipids
Review: ai_reviewed
Evidence:
The cell membrane consists of two layers of phospholipids. Transport proteins are embedded in the layers. The movement of substances across the cell membrane may be by passive or active transport.

### 62. sciq_test_00228 | Biology
What gas is released when dead organisms and other organic materials decompose?

- A: hydrogen peroxide
- B: carbon dioxide
- C: carbon monoxide
- D: nitrous oxide

Answer: B - carbon dioxide
Review: ai_reviewed
Evidence:
Carbon dioxide is given off when dead organisms and other organic materials decompose.

### 63. sciq_test_00865 | Earth and Space Science
What are located along convergent and divergent plate boundaries?

- A: mezas
- B: dunes
- C: volcanoes
- D: megaliths

Answer: C - volcanoes
Review: ai_reviewed
Evidence:
Volcanoes are located along convergent and divergent plate boundaries. They can be found in the middle of plates at hot spots.

### 64. sciq_test_00773 | Physics
What form of matter has a fixed volume but not a fixed shape?

- A: liquid
- B: solid
- C: mixture
- D: gas

Answer: A - liquid
Review: ai_reviewed
Evidence:
Ocean water is an example of a liquid. A liquid is matter that has a fixed volume but not a fixed shape. Instead, a liquid takes the shape of its container. If the volume of a liquid is less than the volume of its container, the top surface will be exposed to the air, like the oil in the bottles in Figure below .

### 65. sciq_test_00153 | Earth and Space Science
Approximately 20% of the atmosphere is made of which element?

- A: nitrogen
- B: oxygen
- C: hydrogen
- D: carbon

Answer: B - oxygen
Review: ai_reviewed
Evidence:
Approximately 20% of the atmosphere is oxygen. This gas is essential for life. In environments where oxygen is in low supply, it can be provided from a tank. Since gases are very compressible, a large amount of oxygen can be stored in a relatively small container. When it is released, the volume expands and the pressure decreases. The gas is then available for breathing under normal pressure.

### 66. sciq_test_00214 | Chemistry
The lattice energy is usually the most important energy factor in determining the stability of what?

- A: harmonic compound
- B: magnetic compound
- C: saline compound
- D: ionic compound

Answer: D - ionic compound
Review: ai_reviewed
Evidence:
The lattice energy is usually the most important energy factor in determining the stability of an ionic compound.

### 67. sciq_test_00680 | Physics
What is the term for materials that have both a defined shape and a defined volume?

- A: gases
- B: solids
- C: liquids
- D: matter

Answer: B - solids
Review: ai_reviewed
Evidence:
Solids are materials that have both a defined shape and a defined volume. They do not take on the shape of their container, as liquids and gases do. Solids can be either amorphous or crystalline. Amorphous solids (such as glass) do not have a well organized three-dimensional arrangement of molecules or atoms, so they lack a high level of order. On the other hand, crystalline solids display a highly ordered and predictable three-dimensional structure. In this section we will discuss the different types of crystalline solids.

### 68. sciq_test_00220 | Biology
Animals are classified according to morphological and developmental characteristics, such as a body plan. with the exception of sponges, the animal body plan is symmetrical. this means that their distribution of body parts is balanced along this?

- A: axis
- B: radius
- C: ulna
- D: skull

Answer: A - axis
Review: ai_reviewed
Evidence:
Classification Features of Animals Animals are classified according to morphological and developmental characteristics, such as a body plan. With the exception of sponges, the animal body plan is symmetrical. This means that their distribution of body parts is balanced along an axis. Additional characteristics that contribute to animal classification include the number of tissue layers formed during development, the presence or absence of an internal body cavity, and other features of embryological development.

### 69. sciq_test_00242 | Earth and Space Science
What is the term for the preserved remains or traces of organisms that lived in the past?

- A: detritis
- B: corals
- C: fossils
- D: bones

Answer: C - fossils
Review: ai_reviewed
Evidence:
Fossils are the preserved remains or traces of organisms that lived in the past. The soft parts of organisms almost always decompose quickly after death. On occasion, the hard parts—mainly bones, teeth, or shells—remain long enough to mineralize and form fossils. An example of a complete fossil skeleton is shown in Figure below . The fossil record is the record of life that unfolded over four billion years and pieced back together through the analysis of fossils.

### 70. sciq_test_00489 | Physics
The medium moves back and forth in the same direction as the wave in what type of wave?

- A: latitudinal wave
- B: longitudinal wave
- C: kinetic wave
- D: variable wave

Answer: B - longitudinal wave
Review: ai_reviewed
Evidence:
In a longitudinal wave, the medium moves back and forth in the same direction as the wave.

### 71. sciq_test_00186 | Biology
Where on a jellyfish is the mouth opening located?

- A: underside
- B: right side
- C: top
- D: left side

Answer: A - underside
Review: ai_reviewed
Evidence:
In the jellyfish, a mouth opening is present on the underside of the animal, surrounded by tentacles bearing nematocysts. Scyphozoans live most of their life cycle as free-swimming, solitary carnivores. The mouth leads to the gastrovascular cavity, which may be sectioned into four interconnected sacs, called diverticuli. In some species, the digestive system may be further branched into radial canals. Like the septa in anthozoans, the branched gastrovascular cells serve two functions: to increase the surface area for nutrient absorption and diffusion; thus, more cells are in direct contact with the nutrients in the gastrovascular cavity. In scyphozoans, nerve cells are scattered all over the body. Neurons may even be present in clusters called rhopalia. These animals possess a ring of muscles lining the dome of the body, which provides the contractile force required to swim through water. Scyphozoans are dioecious animals, that is, the sexes are separate. The gonads are formed from the gastrodermis and gametes are expelled through the mouth. Planula larvae are formed by external fertilization; they settle on a substratum in a polypoid form known as scyphistoma. These forms may produce additional polyps by budding or may transform into the medusoid form. The life cycle (Figure 28.10) of these animals can be described as polymorphic, because they exhibit both a medusal and polypoid body plan at some point in their life cycle.

### 72. sciq_test_00105 | Physics
Anything moving has what type of energy?

- A: magnetic
- B: thermal
- C: potential
- D: kinetic

Answer: D - kinetic
Review: ai_reviewed
Evidence:
Why do the air and sand of Death Valley feel so hot? It’s because their particles are moving very rapidly. Anything that is moving has kinetic energy, and the faster it is moving, the more kinetic energy it has. The total kinetic energy of moving particles of matter is called thermal energy . It’s not just hot things such as the air and sand of Death Valley that have thermal energy. All matter has thermal energy, even matter that feels cold. That’s because the particles of all matter are in constant motion and have kinetic energy.

### 73. sciq_test_00177_adapted_v2 | Physics
An object has an applied force and an opposing frictional force along one line, with all other forces balanced. What is the applied force minus friction?

- A: quarter force
- B: rolled force
- C: kinetic force
- D: net force

Answer: D - net force
Review: ai_reviewed_adaptation
Evidence:
The net force is found by subtracting the frictional force from the applied force.

### 74. sciq_test_00332 | Biology
The left atrium receives oxygen-rich blood from which organs?

- A: pancreas
- B: lungs
- C: brain
- D: liver

Answer: B - lungs
Review: ai_reviewed
Evidence:
The left atrium receives oxygen-rich blood from the lungs.

### 75. sciq_test_00744 | Chemistry
Reactants may also be present in such low concentrations that it is unlikely they will meet and do what?

- A: depart
- B: melt
- C: collide
- D: explode

Answer: C - collide
Review: ai_reviewed
Evidence:
Most chemical reactions within organisms would be impossible under the normal conditions within cell. For example, the body temperature of most organisms is too low for reactions to occur quickly enough to carry out life processes. Reactants may also be present in such low concentrations that it is unlikely they will meet and collide. Therefore, the rate of most biochemical reactions must be increased by a catalyst. A catalyst is a chemical that speeds up chemical reactions. In organisms, catalysts are called enzymes .

### 76. sciq_test_00021 | Biology
Presence of a cell wall, large central vacuole, and organelles called plastids distinguish what type of cell?

- A: reproductive
- B: heterotroph
- C: animal
- D: plant

Answer: D - plant
Review: ai_reviewed
Evidence:
All but one of the structures described above are found in plant cells as well as animal cells. The only exception is centrioles, which are not found in plant cells. Plant cells have three additional structures that are not found in animals cells. These include a cell wall, large central vacuole, and organelles called plastids. You can see these structures in the model of a plant cell in Figure below . You can also see them in the interactive plant cell at this link:.

### 77. sciq_test_00960 | Biology
Where do t cells mature?

- A: bone marrow
- B: pituitary gland
- C: liver
- D: thymus gland

Answer: D - thymus gland
Review: ai_reviewed
Evidence:
Both types of lymphocytes are produced in the red bone marrow. They are named for the sites where they grow larger. The "B" in B cells stands for “bone. ” B cells grow larger in red bone marrow. The "T" in T cells stands for “thymus. ” T cells mature in the thymus gland.

### 78. sciq_test_00308 | Earth and Space Science
What kind of rock layer makes up the bottom of an aquifer?

- A: porous
- B: invisible
- C: crystalline
- D: impermeable

Answer: D - impermeable
Review: ai_reviewed
Evidence:
A rock layer must be porous and permeable to be a good aquifer. An impermeable layer makes up the bottom of an aquifer.

### 79. sciq_test_00862 | Biology
Hepatitis b is inflammation of which organ?

- A: the kidney
- B: the liver
- C: the brain
- D: the colon

Answer: B - the liver
Review: ai_reviewed
Evidence:
Hepatitis B is inflammation of the liver caused by infection with the hepatitis B virus. In many people, the immune system quickly eliminates the virus from the body. However, in a small percentage of people, the virus remains in the body and continues to cause illness. It may eventually damage the liver and increase the risk of liver cancer, which is usually fatal.

### 80. sciq_test_00506 | Biology
Channel proteins form what in the membrane?

- A: pores
- B: fibers
- C: atoms
- D: walls

Answer: A - pores
Review: ai_reviewed
Evidence:
Channel proteins form pores, or tiny holes, in the membrane. This allows water molecules and small ions to pass through the membrane without coming into contact with the hydrophobic tails of the lipid molecules in the interior of the membrane.

### 81. sciq_test_00235 | Biology
Enzymes can catalyze up to several million reactions per what?

- A: minute
- B: day
- C: second
- D: hour

Answer: C - second
Review: ai_reviewed
Evidence:
Enzymes are extremely efficient in speeding up biochemical reactions. They can catalyze up to several million reactions per second. As a result, the difference in rates of biochemical reactions with and without enzymes may be enormous. A typical biochemical reaction might take hours or even days to occur under normal cellular conditions without an enzyme, but less than a second with the enzyme.

### 82. sciq_test_00736 | Chemistry
What is the separation of ions that occurs when a solid ionic compound dissolves?

- A: combustion
- B: decomposition
- C: inflammation
- D: dissociation

Answer: D - dissociation
Review: ai_reviewed
Evidence:
Dissociation is the separation of ions that occurs when a solid ionic compound dissolves.

### 83. sciq_test_00403 | Physics
The amount of heat required to raise a single mass unit of a substance by a single temperature unit is known as what?

- A: solitary heat
- B: temperature variation
- C: specific heat
- D: specific gravity

Answer: C - specific heat
Review: ai_reviewed
Evidence:
When heat flows into an object, its thermal energy increases and so does its temperature. The amount of temperature increase depends on three things: 1) how much heat was added, 2) the size of the object, and 3) the material of which the object is made. When you add the same amount of heat to the same mass of different substances, the amount of temperature increase is different. Each substance has a specific heat, which is the amount of heat necessary to raise one mass unit of that substance by one temperature unit.

### 84. sciq_test_00465_adapted_v2 | Physics
Which property of the fiber and its surrounding coating must be appropriately chosen to permit total internal reflection?

- A: wavelength
- B: electromagnetic index
- C: refractive index
- D: reflective point

Answer: C - refractive index
Review: ai_reviewed_adaptation
Evidence:
The index of refraction outside the fiber must be smaller than inside, a condition that is easily satisfied by coating the outside of the fiber with a material having an appropriate refractive index.

### 85. sciq_test_00245 | Chemistry
The force of attraction between a positively charged metal ion and the valence electrons it shares with other ions of the metal is called?

- A: temporal bond
- B: ionic bond
- C: metallic yield
- D: metallic bond

Answer: D - metallic bond
Review: ai_reviewed
Evidence:
A metallic bond is the force of attraction between a positively charged metal ion and the valence electrons it shares with other ions of the metal. The electrons move freely around the positive ions, which form a lattice-like structure.

### 86. sciq_test_00770 | Physics
No charge is actually created or destroyed when charges are separated as we have been discussing. rather, existing charges are moved about. in fact, in all situations the total amount of charge is always this?

- A: smaller
- B: less
- C: constant
- D: more

Answer: C - constant
Review: ai_reviewed
Evidence:
No charge is actually created or destroyed when charges are separated as we have been discussing. Rather, existing charges are moved about. In fact, in all situations the total amount of charge is always constant. This universally obeyed law of nature is called the law of conservation of charge. Law of Conservation of Charge Total charge is constant in any process.

### 87. sciq_test_00239 | Biology
What makes up the dense outer layer of bones?

- A: compact bone
- B: adipose tissue
- C: ligaments
- D: plasma

Answer: A - compact bone
Review: ai_reviewed
Evidence:
Compact bone makes up the dense outer layer of bone. It is very hard and strong.

### 88. sciq_test_00698_adapted_v2 | Physics
Two wires have the same material, length and temperature. Which property is greater for the narrower wire?

- A: wattage
- B: current
- C: resistance
- D: voltage

Answer: C - resistance
Review: ai_reviewed_adaptation
Evidence:
A wide wire has less resistance than a narrow wire of the same material. Electricity flowing through a wire is like water flowing through a hose. More water can flow through a wide hose than a narrow hose. In a similar way, more current can flow through a wide wire than a narrow wire.

### 89. sciq_test_00603 | Biology
What is the only animal phyla that does not consist exclusively of invertebrates?

- A: bacteria
- B: chordates
- C: arthropods
- D: eukaryotes

Answer: B - chordates
Review: ai_reviewed
Evidence:
Except for the chordates, all animal phyla consist only of invertebrates.

### 90. sciq_test_00723 | Physics
What do you call materials able to conduct electricity with 100% efficiency, meaning that no energy is lost during the electrical transmission?

- A: superconductors
- B: poor conductors
- C: super-insulators
- D: electromagnets

Answer: A - superconductors
Review: ai_reviewed
Evidence:
Many chemists are currently working in the field of superconductivity. Superconductors are materials that are able to conduct electricity with 100% efficiency, meaning that no energy is lost during the electrical transmission, as happens with conventional conducting materials like copper cable. The challenge is to design materials that can act as superconductors at normal temperatures, as opposed to only being able to superconduct at very low temperatures.

### 91. sciq_test_00714 | Biology
What type of organism generally lives in or on its host?

- A: predator
- B: insect
- C: parasite
- D: bacteria

Answer: C - parasite
Review: ai_reviewed
Evidence:
A parasite generally lives in or on its host. An example of a parasite that lives in its host is the hookworm. Figure below shows two hookworms living inside a human host’s intestines. The hookworms obtain nutrients and shelter from their host, which is harmed by the loss of nutrients and blood.

### 92. sciq_test_00272 | Biology
If the dna from all 46 chromosomes in a human cell nucleus was laid out end to end, it would measure approximately how long?

- A: one meter
- B: two meters
- C: three meters
- D: four meters

Answer: B - two meters
Review: ai_reviewed
Evidence:
Eukaryotic Chromosomal Structure and Compaction If the DNA from all 46 chromosomes in a human cell nucleus was laid out end to end, it would measure approximately two meters; however, its diameter would be only 2 nm. Considering that the size of a typical human cell is about 10 µm (100,000 cells lined up to equal one meter), DNA must be tightly packaged to fit in the cell’s nucleus. At the same time, it must also be readily accessible for the genes to be expressed. During some stages of the cell cycle, the long strands of DNA are condensed into compact chromosomes. There are a number of ways that chromosomes are compacted. In the first level of compaction, short stretches of the DNA double helix wrap around a core of eight histone proteins at regular intervals along the entire length of the chromosome (Figure 10.4). The DNA-histone complex is called chromatin. The beadlike, histone DNA complex is called a nucleosome, and DNA connecting the nucleosomes is called linker DNA. A DNA molecule in this form is about seven times shorter than the double helix without the histones, and the beads are about 10 nm in diameter, in contrast with the 2-nm diameter of a DNA double helix. The next level of compaction occurs as the nucleosomes and the linker DNA between them are coiled into a 30-nm chromatin fiber. This coiling further shortens the chromosome so that it is now about 50 times shorter than the extended form. In the third level of packing, a variety of fibrous proteins is used to pack the chromatin. These fibrous proteins also ensure that each chromosome in a non-dividing cell occupies a particular area of the nucleus that does not overlap with that of any other chromosome (see the top image in Figure 10.3).

### 93. sciq_test_00450 | Biology
What two types of tissue compose most of the non-pregnant and non-lactating female breast?

- A: scar and collagenous
- B: intestine and collagenous
- C: adipose and collagenous
- D: silicone and collagenous

Answer: C - adipose and collagenous
Review: ai_reviewed
Evidence:
Structure of the Lactating Breast Mammary glands are modified sweat glands. The non-pregnant and non-lactating female breast is composed primarily of adipose and collagenous tissue, with mammary glands making up a very minor proportion of breast volume. The mammary gland is composed of milk-transporting lactiferous ducts, which expand and branch extensively during pregnancy in response to estrogen, growth hormone, cortisol, and prolactin. Moreover, in response to progesterone, clusters of breast alveoli bud from the ducts and expand outward toward the chest wall. Breast alveoli are balloon-like structures lined with milk-secreting cuboidal cells, or lactocytes, that are surrounded by a net of contractile myoepithelial cells. Milk is secreted from the lactocytes, fills the alveoli, and is squeezed into the ducts. Clusters of alveoli that drain to a common duct are called lobules; the lactating female has 12–20 lobules organized radially around the nipple. Milk drains from lactiferous ducts into lactiferous sinuses that meet at 4 to 18 perforations in the nipple, called nipple pores. The small bumps of the areola (the darkened skin around the nipple) are called Montgomery glands. They secrete oil to cleanse the nipple opening and prevent chapping and cracking of the nipple during breastfeeding.

### 94. sciq_test_00860 | Chemistry
What element is present in all organic molecules?

- A: hydrogen
- B: oxygen
- C: sodium
- D: carbon

Answer: D - carbon
Review: ai_reviewed
Evidence:
The Carbon Cycle Carbon is the fourth most abundant element in living organisms. Carbon is present in all organic molecules, and its role in the structure of macromolecules is of primary importance to living organisms. Carbon compounds contain energy, and many of these compounds from plants and algae have remained stored as fossilized carbon, which humans use as fuel. Since the 1800s, the use of fossil fuels has accelerated. As global demand for Earth’s limited fossil fuel supplies has risen since the beginning of the Industrial Revolution, the amount of carbon dioxide in our atmosphere has increased as the fuels are burned. This increase in carbon dioxide has been associated with climate change and is a major environmental concern worldwide.

### 95. sciq_test_00139 | Biology
What are the smallest structural and functional unit of all living organisms?

- A: cells
- B: lipids
- C: neutrons
- D: proteins

Answer: A - cells
Review: ai_reviewed
Evidence:
If you zoom in very close on a leaf of a plant, or on the skin on your hand, or a drop of blood, you will find cells, you will find cells ( Figure below ). Cells are the smallest structural and functional unit of all living organisms. Most cells are so small that they are usually visible only through a microscope. Some organisms, like bacteria, plankton that live in the ocean, or the Paramecium, shown in Figure below , are unicellular, made of just one cell. Other organisms have millions, billions, or trillions of cells.

### 96. sciq_test_00414_adapted_v2 | Earth and Space Science
Which telescope category is defined by detecting radio waves?

- A: X-ray telescopes
- B: ultraviolet telescopes
- C: radio telescopes
- D: infrared telescopes

Answer: C - radio telescopes
Review: ai_reviewed_adaptation
Evidence:
Radio telescopes collect and focus radio waves from distant objects.

### 97. sciq_test_00189_adapted_v2 | Earth and Space Science
What distance unit is defined as the distance light travels in one year?

- A: astronomical unit
- B: parsec
- C: light years
- D: kilometers

Answer: C - light years
Review: ai_reviewed_adaptation
Evidence:
Astronomers use light years as the unit to describe distances in space. Remember that a light year is the distance light travels in one year.

### 98. sciq_test_00218 | Earth and Space Science
In astronomy, what are so dense that not even light can escape their gravity?

- A: black rods
- B: red holes
- C: black holes
- D: dwarf stars

Answer: C - black holes
Review: ai_reviewed
Evidence:
If the core remaining after a supernova is more than about 5 times the mass of the Sun, the core collapses to become a black hole . Black holes are so dense that not even light can escape their gravity. For that reason, we can't see black holes. How can we know something exists if radiation can't escape it? We know a black hole is there by the effect that it has on objects around it. Also, some radiation leaks out around its edges. A black hole isn't a hole at all. It is the tremendously dense core of a supermassive star.

### 99. sciq_test_00805 | Physics
What do we call a simple machine that consists of a rope and grooved wheel?

- A: pedal
- B: axle
- C: lever
- D: pulley

Answer: D - pulley
Review: ai_reviewed
Evidence:
A pulley is a simple machine that consists of a rope and grooved wheel. Single pulleys may be fixed or moveable. Single and moveable pulleys may be combined in a compound pulley. The ideal mechanical advantage of a pulley or compound pulley is always equal to or greater than 1. Fixed pulleys and some compound pulleys also change the direction of the input force.

### 100. sciq_test_00746 | Earth and Space Science
What is the term for what the earth rotates on?

- A: axis
- B: tip
- C: compass
- D: radius

Answer: A - axis
Review: ai_reviewed
Evidence:
This Concept deals with some Earth basics. Earth is a planet and has the characteristics of a planet. Like other planets, it is nearly round. This is because it has enough mass for its gravity to pull material into a round shape. Earth's gravity has also pulled in small objects, like asteroids. So the planet's orbit is cleared. Earth rotates on its axis and revolves around its star. As a result of its rotation, Earth has a day-night cycle. The tilt of its axis creates the seasons. Earth has layers from crust to mantle to core. The core is divided into a liquid outer core and a solid inner core. The liquid outer core has convection, which generates the magnetic field. The mantle is solid rock. The crust has two major types: continental and oceanic. The crust and uppermost mantle make up the lithosphere. Beneath the lithosphere is the asthenosphere. The lithosphere is brittle and will break. The asthenosphere can flow.


## Historical audit and traceability

Version 1 had 16 flagged issues, all addressed editorially in the version-2 adaptations above. Historical machine-readable files are retained in data/evaluation/quality_audit.json, evaluation_replacements.json and evaluation_adaptations_v2.json. The current 100-item artifact is phase1_evaluation_v2.json; it is AI-reviewed within the limitations stated above. Original candidates and review versions are provenance, not additional final evaluation sets.
