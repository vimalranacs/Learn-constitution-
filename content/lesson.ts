export const parliamentLesson = {
  id:'parliament-composition', version:1, title:'Meet Parliament',
  subtitle:'One institution. Three constitutional components.',
  objectives:['Name the three components of Parliament.','Distinguish Parliament from either one of its Houses.'],
  graphNodeIds:['art_79','inst_parliament'], sourceIds:['src_const_2026_leg'],
  sections:[
    {title:'Begin with a naming puzzle',text:'Imagine reading two headlines: “The House of the People debates a proposal” and “Parliament considers a proposal.” Are the names interchangeable? Before following the news, it helps to know how the institution is put together. This is an illustrative reading exercise, not a description of a particular Bill.'},
    {title:'An institution can have several parts',text:'A useful first distinction is between a whole institution and one of its components. Think of a book and its chapters: a chapter belongs to the book, but is not the whole book. This analogy explains membership only; it says nothing about constitutional powers or hierarchy.'},
    {title:'What the Constitution establishes',text:'Article 79 provides for a Parliament for the Union consisting of the President and two Houses: the Council of States and the House of the People. The President is a component of Parliament under this provision, but is not a third House. Composition does not mean that all three have identical functions.'},
    {title:'Read the diagram as composition',text:'The three branches below mean “consists of”. They do not mean “commands”, “appoints” or “is superior to”. Learning to read the type of a relationship is essential: a constitutional map should explain the connection, not merely draw an arrow.'}
  ],
  question:'A friend says: “The House of the People is the whole of Parliament.” Which correction follows from Article 79?',
  answers:[
    {text:'It is one of two Houses; Parliament also includes the Council of States and the President.',correct:true,feedback:'Yes. You distinguished the whole institution from a component and included all three components named in Article 79.'},
    {text:'Parliament consists only of its two Houses.',correct:false,feedback:'That leaves out the President, who is expressly included in Article 79. Identify the whole list in the source passage.'},
    {text:'The President is the third House of Parliament.',correct:false,feedback:'Article 79 names the President and two Houses. Being a component of Parliament does not make the President a House.'}
  ],
  recap:'Parliament consists of the President, the Council of States and the House of the People. An institution’s composition and its members’ powers are different questions.'
};
