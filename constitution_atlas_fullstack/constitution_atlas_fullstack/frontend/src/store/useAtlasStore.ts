import { create } from 'zustand';

export type DepthLevel = 'beginner' | 'intermediate' | 'advanced' | 'research';
export type ActiveTab = 'graph' | 'reader' | 'simulations' | 'trace_power' | 'timeline' | 'philosophy' | 'sources' | 'workspace' | 'validation';

interface AtlasState {
  activeNodeId: string;
  selectedNodes: string[];
  breadcrumbs: string[];
  bookmarks: string[];
  notes: Record<string, string>;
  depthLevel: DepthLevel;
  activeTab: ActiveTab;
  filterType: string;
  searchQuery: string;
  setActiveNode: (id: string) => void;
  toggleBookmark: (id: string) => void;
  saveNote: (id: string, text: string) => void;
  setDepthLevel: (level: DepthLevel) => void;
  setActiveTab: (tab: ActiveTab) => void;
  setFilterType: (type: string) => void;
  setSearchQuery: (q: string) => void;
}

export const useAtlasStore = create<AtlasState>((set) => ({
  activeNodeId: 'const_india',
  selectedNodes: ['const_india'],
  breadcrumbs: ['const_india'],
  bookmarks: ['art_21', 'inst_parliament', 'judg_kesavananda', 'phil_privacy'],
  notes: {},
  depthLevel: 'intermediate',
  activeTab: 'graph',
  filterType: 'ALL',
  searchQuery: '',
  setActiveNode: (id) =>
    set((state) => ({
      activeNodeId: id,
      breadcrumbs: state.breadcrumbs.includes(id)
        ? state.breadcrumbs
        : [...state.breadcrumbs.slice(-14), id],
    })),
  toggleBookmark: (id) =>
    set((state) => ({
      bookmarks: state.bookmarks.includes(id)
        ? state.bookmarks.filter((b) => b !== id)
        : [...state.bookmarks, id],
    })),
  saveNote: (id, text) =>
    set((state) => ({
      notes: { ...state.notes, [id]: text },
    })),
  setDepthLevel: (depthLevel) => set({ depthLevel }),
  setActiveTab: (activeTab) => set({ activeTab }),
  setFilterType: (filterType) => set({ filterType }),
  setSearchQuery: (searchQuery) => set({ searchQuery }),
}));
