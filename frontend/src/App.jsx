import Header from './components/Header';
import NewsChecker from './components/NewsChecker';
import Footer from './components/Footer';

function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <main>
        <NewsChecker />
      </main>
      <Footer />
    </div>
  );
}

export default App;